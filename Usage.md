# Using cports

This document provides a comprehensive reference on using the `cports` system,
more specifically its `cbuild` component.

*Table of Contents*

* [Introduction](#introduction)
* [Getting Started](#getting_stated)
  * [Requirements](#requirements)
  * [How It Works](#how_it_works)
  * [Preparing](#preparing)
  * [Build Root Setup](#root_setup)
  * [Building a Package](#building_package)
* [Bootstrapping](#bootstrapping)
  * [Bootstrap Requirements](#bootstrap_requirements)
  * [Bootstrap Process](#bootstrap_process)
  * [Using Incompatible Hosts](#incompatible_host)
* [Cbuild Reference](#cbuild_reference)
  * [Optional Arguments](#optional_arguments)
  * [Commands](#commands)
  * [Configuration File](#config_file)
* [Cross Compiling](#cross_compiling)
* [Ccache](#ccache)
* [Help](#help)

<a id="introduction"></a>
## Introduction

The `cports` collection comes with a specialized build system, `cbuild`. The
system provides a way for people to build their own binary packages from
special templates.

If you are looking for instructions on how to write templates, refer to the
`Packaging.md` instead.

<a id="getting_started"></a>
## Getting Started

In order to get started with the system, your operating system environment must
satisfy some requirements. After that, you can use it to build and manage packages,
assuming you have bootstrapped the system.

<a id="requirements"></a>
### Requirements

**TL;DR:** You need a handful of tools, mainly Python and a few binaries mentioned
in the list below. You need a 3.8+ kernel with support for namespaces, including
user namespaces, and cgroups. You need to run as a regular user, and not in a
`chroot`.

The `cbuild` tool has relatively few dependencies. You can usually find all of
them in any Linux distribution. Additionally, it imposes some requirements on
the Linux kernel you are running.

The userland dependencies are the following:

* Python (3.x series; any recent version should do)
* `scanelf` (from `pax-tools`)
* `apk` (from `apk-tools`)
* `openssl`
* `git` (optional; required for reproducibility)
* `bwrap` (from `bubblewrap`)
* `tee`

You also need Linux kernel 3.8 or newer, with namespaces and cgroups enabled.
Notably the following options must be enabled:

* `CONFIG_NAMESPACES=y`
* `CONFIG_UTS_NS=y`
* `CONFIG_IPC_NS=y`
* `CONFIG_USER_NS=y`
* `CONFIG_PID_NS=y`
* `CONFIG_NET_NS=y`
* `CONFIG_CGROUPS=y`

You can check for those with something like `zgrep /proc/config.gz` or
alternatively `grep /boot/config-$(uname -r)`.

Most distribution kernels should have the options enabled by default.

In addition to these, you must run the system under a normal user. Running as
the `root` user will result in early failure.

The environment used to run `cbuild` must not be a `chroot`. Running inside
of a `chroot` interferes with the sandbox/namespaces. If you really need to
use a custom root, you can use `bwrap` to provide functionality equivament
to `chroot`, as there is nothing preventing nesting namespaces. The command
would be something like the following:

```
$ bwrap --unshare-user --bind /path/to/my/root / --dev /dev --proc /proc --tmpfs /tmp /bin/sh
```

If you satisfy all this, you should be good to go.

<a id="how_it_works"></a>
### How It Works

**TL;DR:** Packages are built in a sandboxed container with limited access to
the outside environment. The system automatically manages a local repository
for you, including package signing. Dependencies are installed in the sandbox,
software is built, packages are created, and cleanup is performed. The system
can build software recursively, so you can give it a metapackage to build and
it will do the whole dependency tree.

If you are familiar with Void Linux's `xbps-src`, the system should immediately
appear familiar to you. You should not consider it a clone, since it was written
from scratch in a completely different language and does a lot of things in a
different way, but you will notice a lot of similarities.

When building packages with `cbuild`, the build process happens in a minimal
container. This is what you need namespaces for; they are the building blocks
of this container.

This container is made up of a minimal collection of Chimera packages, which
provide the initial environment. We call it the *build root*. It is essentially
a sandbox with different restrictions depending on the phase of the build.

Most of the time, the build root is:

* Read only - after installing dependencies, programs run within are not allowed
  to write outside of their designated directories.
* Without network access - after fetching all source distfiles, programs are not
  allowed to access the network from within. This enforces the policy of having
  to fetch all of their files ahead of time. Checksums are enforced for those
  files.
* Isolated - the sandbox does not have access to the outside file system.
* Unprivileged - after the fetch stage, all namespace types are unshared.

When building a package, the following happens, in simplified terms:

* Build dependencies are installed in the sandbox, provided they are available.
  If some dependency is unavailable, it is built first, using the same process.
  This can happen recursively.
* All declared source distfiles are fetched, if not already cached. They are
  subsequently verified (the checksums must match what the template declares).
  If this fails, the fetch is re-tried.
* Source distfiles are extracted and patches are applied if necessary.
* The software is configured and built within the sandbox.
* Files are installed in a special `destdir`. Outside of this, the directory
  where files are extracted, the `/tmp` directory in the sandbox and potential
  cache directories (e.g. for `ccache`), the entire sandbox is read only during
  all steps after installing dependencies.
* Packages are created in the local repository and signed.

If you are familiar with `xbps-src`, these are the main conceptual differences:

* Most `cbuild` code is run outside the sandbox. Only specific commands are run
  within, which includes dependency installation, distfiles extraction, patching,
  and the build itself. Once files are installed, `cbuild` handles the rest on
  its own without involving the container. In contrast, `xbps-src` will reexec
  itself inside its sandbox and run everything there.
* The sandboxing is much more advanced and more strictly enforced. With `xbps-src`
  you don't get any warranty that the build container is intact after anything
  is run within. In contrast, `cbuild` guarantees that the sandbox is exactly
  the same before and after building something in it.
* The `cbuild` system has no concept of `hostdir`, instead preferring fine
  grained control over every directory.
* While `xbps-src` provides a "temporary build root" functionality, `cbuild`
  does not. This is because doing so would introduce reliance on `overlayfs`
  and a custom `suid` binary. This would prevent us from sandboxing properly.
  However, this functionality is not needed, since we guarantee consistency of
  the sandbox at all times. For parallel building of several packages at once,
  the `-t` flag still exists. Instead of using an overlay, it will simply
  bootstrap a fresh temporary root. Unlike with `xbps-src`, this does not
  create a performance problem, as everything is much faster.
* Created packages are automatically signed. With `xbps-src` this would be a
  potential security hazard, but `cbuild` can guarantee no malicious process
  can get access to your signing keys. That means repositories generated with
  `cbuild` are ready to be deployed in remote locations.
* There is only one profile for each architecture for both native and cross
  builds.

<a id="preparing"></a>
### Preparing

You will need to generate a signing key. You can do that like this:

```
$ ./cbuild.py keygen
```

You can optionally pass your own private key name or path as an argument. If
you don't do that, it will be assigned an automatic name consisting of your
Git email address (or system username if not available) and a timestamp, plus
the `.rsa` extension. Your public key will be stored in the same location,
but the extension will be `.pub`.

An optional second argument can specify the key size, which is 2048 by default.

Keys are by default stored in `etc/keys`.

Once generated, the tool will automatically update the configuration file you
have, which is `etc/config.ini` by default, with the correct key path.

If you don't have a key generated and set, you will not be able to build
packages. It is possible to override this with `--allow-unsigned`, but it
is not recommended to do that.

<a id="root_setup"></a>
### Build Root Setup

Since Chimera currently does not provide any binary packages, if you are using
the system for the first time, you first need to bootstrap it from source. In
order to do that, please refer to the [bootstrapping](#bootstrapping) section.

To create a build root:

```
$ ./cbuild.py binary-bootstrap
```

By default, this will be `bldroot` inside your `cports` directory. If you have
just done a source bootstrap, there is a chance you don't need to run this as
the source bootstrap does it for you as the last step. You will need to do this
if you ever need to re-create it.

<a id="building_package"></a>
### Building a Package

Then, the only thing left to do is to pick a package to build. Let's say, `awk`
from the `main` category. You need to run this:

```
$ ./cbuild.py pkg main/awk
```

This will parse `main/awk/template.py` and build it according to the metadata
and routines declared in the template.

That's it!

<a id="bootstrapping"></a>
## Bootstrapping

By this, it is meant bootstrapping from source. Since the distribution currently
does not provide any binary packages, this is something you will always need
to do.

Bootstrapping has more requirements than simply using the system.

<a id="bootstrap_requirements"></a>
### Bootstrap Requirements

The base requirements of `cbuild` still apply. You also need to be running a
system based on the `musl` C library. This can be for example Void Linux or
Alpine Linux. Void Linux is most widely tested. You can also use Chimera itself.

The system must contain an initial toolchain. It consists of these:

* `clang` with `lld`, `libc++`, `compiler-rt` and LLVM `libunwind`
* `cmake`
* `meson`
* `patch`
* `pkg-config` (`pkgconf` or the regular one)
* GNU `make` (called `gmake` or `make`)
* NetBSD `make` (called `bmake` or `make`)
* `ninja`
* `strip`
* `byacc`
* `flex`
* `perl`
* `m4`

These can all be found in most distributions' package collections.

<a id="bootstrap_process"></a>
### Bootstrap Process

Chimera uses a 3-stage bootstrap process. It is largely automatic and hidden
from you. You can invoke it like:

```
$ ./cbuild.py bootstrap
```

Optionally you can stop the process at a specific stage by passing its number
as an argument (not when using `bootstrap.sh`).

To explain what's going on:

* Stage 0 is software built inside the system you are running.
* Stage 1 is software built inside the system assembled from stage 0.
* Stage 2 is software built inside the system assembled from stage 1.

The stage 2 is considered final. Every stage results in a regular build root
that can be used to build software. However, since stage 0 is built using your
host software, it is considered raw and not reproducible, and may be affected
by toolchain choices made within the host.

Stage 1 is more refined, as it was built inside a semi-controlled Chimera
environment. However, since the build root was created using software built
with a toolchain that is not controlled, it is considered dirty.

Stage 2 is built only using a toolchain that was built with Chimera. It should
at this point be free of external influences, and considered final.

You will have the following artifacts:

* `bldroot-stage0` is the build root that was assembled from packages originally
  built on the host system.
* `bldroot-stage1` is the build root assembled from stage 1 packages.
* `bldroot` is the final build root; if you remove it and `binary-bootstrap`,
  you will get the same thing.
* `packages-stage0` is the repository of packages `bldroot-stage0` is created
  from.
* `packages-stage1` is the repository of packages `bldroot-stage1` is created
  from.
* `packages` is the final repository.
* `sources` is the source distfiles cache, shared for all.

You can remove all the `*-stage*` directories if you want. They are present
mostly for inspection.

If the bootstrap fails at any point, you can start it again and it will continue
where it left off. No things already built will be built again.

<a id="incompatible_host"></a>
### Using Incompatible Hosts

If you do not have a suitable system for bootstrapping (for example a `glibc`
based system), you do not need to go out of your way to set one up. The `cports`
tree provides the `bootstrap.sh` script for this purpose.

This works by fetching a compatible `rootfs` (Void Linux with `musl`) and then
running regular bootstrap within. It uses `bwrap` for this, so you should never
run it as `root`.

Any arguments passed to the script are passed to `cbuild.py`. This is most useful
for passing the number of build jobs (e.g. `-j16` to use 16 threads). You can not
use it to pass the stage number directly like you can pass to `bootstrap`, since
the positional and optional arguments are order sensitive (positional arguments
come after optional ones) and these are passed before the `bootstrap` command.
If you need to override this, you can use the `BOOTSTRAP_STAGE` environment
variable.

**NOTE:** You still need to prepare as usual. That means generating a signing
key and setting up the configuration file as necessary. Once the process finishes,
you will have your packages and build root ready, and you will no longer need to
use the script.

**NOTE:** You should avoid using absolute paths to artifact directories and the
build root when using the script, as the whole process is contained in its own
special root and these absolute paths will not resolve. Only use relative paths
within the `cports` tree.

If the process fails during stage 0, you will probably want to fix the problem
and resume it. To prevent the script from starting from scratch, set the variable
`BOOTSTRAP_ROOT` in your environment to the path to the directory with the root
you already have. This will make it proceed instead.

If the process fails during any other stage, you no longer need to use the script
(though there is nothing preventing you from doing so). Once stage 0 is finished,
you already have a suitable root in place, so you can run `cbuild.py bootstrap`
directly in your own system.

<a id="cbuild_reference"></a>
## Cbuild Reference

Every `cbuild` action consists of the following:

```
$ ./cbuild.py [optional arguments] COMMAND [command arguments]
```

The order of reading settings is the following:

1) Optional arguments or command arguments
2) Configuration file
3) Default value

That is, if you pass a setting on the command line, it is always prefered.
Otherwise, it is read from the configuration file. If this is not possible,
the default value is used.

<a id="optional_arguments"></a>
### Optional Arguments

Optional arguments are global, separate from the command. However, some of them
only have an effect with specific commands.

* `--allow-unsigned` Do not sign packages and allow building without a signing
  key set up.
* `-a ARCH`, `--arch ARCH` Build for architecture `ARCH`, possibly cross compiling.
* `-b ROOT`, `--build-root ROOT` *(default: `bldroot`)* Set the path to the build
  root to use.
* `-c PATH`, `--config PATH` *(default: `etc/config.ini`)* The path to the config
  file that `cbuild` reads configuration data from.
* `-C`, `--skip-check` Never attempt to run the `check` phase.
* `-f`, `--force` Packages will be created and overwritten even if one already
  exists in the local repository.
* `-g`, `--build-dbg` Always build `-dbg` packages.
* `-I`, `--skip-dependencies` Skip installation of dependencies in the `bldroot`,
  as well as removal of automatic dependencies after successful build.
* `-j JOBS`, `--jobs JOBS` *(default: 1)* The number of build jobs to use. You
  will usually want to set this to the number of CPU threads you have, unless
  limited by memory.
* `-K`, `--keep-temporary` Keep temporary build files after a successful build,
  this includes the `builddir` and `destdir`. If using a temporary build root,
  it will not be removed.
* `-L`, `--no-color` Color output will be suppressed. By default color output
  is used, unless `NO_COLOR` is set in the environment or the output is being
  redirected/piped.
* `-N`, `--no-remote` Never use remote repositories to fetch dependencies.
* `-r REPO`, `--repository-path REPO` *(default: `packages`)* Set the path to the
  local repository to build packages in.
* `-s SOURCES`, `--sources-path SOURCES` *(default: `sources`)* Set the path to the
  source distfiles cache.
* `-t`, `--temporary` Create a temporary `bldroot` for the build. The `-b` argument
  is used as a base path as well as the name prefix for the temporary root if
  provided. The temporary root is removed at the end (whether the build succeeded
  or failed) unless `--keep-temporary` is passed.

<a id="commands"></a>
### Commands

The following commands are recognized:

* `binary-bootstrap [ARCH]` Create a build root from local packages. The local
  repository must be populated, or a sufficient remote repository must be
  available. Optionally, you can pass an architecture name to create a build
  root of. The architecture's binaries must be runnable on the current kernel.
  This is typically only useful for e.g. using 32-bit build roots on 64-bit
  hosts with compatible architectures.
* `bootstrap [STAGE]` Bootstrap from source. If `STAGE` is passed, stop at that
  stage (number). By default, that is `2`. Stage 0 bootstrap must be run in a
  compatible host system.
* `bootstrap-update` Update the packages in your build root to latest.
* `chroot` Enter the build root with an interactive shell. In this environment,
  the root is mostly unsandboxed, i.e. writable and with network access. You
  can use this kind of environment for quick testing, as well as entering failed
  builds and inspecting them.
* `clean` Clean up the build root. This means removing automatic dependencies
  and removing `builddir` and `destdir` within.
* `keygen [KEYPATH [KEYSIZE]]` Generate your signing key. You can optionally
  specify the key name (if not a path, will be stored in the default location
  of `etc/keys`), key path, and key size (2048 by default). The configuration
  file will automatically be updated. You can also pre-specify the key path
  or name in the configuration file ahead of time, in which case it will use
  those, unless overridden on the command line. The system will not overwrite
  keys that already exist (i.e. if a valid key is specified in configuration,
  this will fail).
* `prune-obsolete` Prune obsolete packages within all repositories for the
  current architecture (can be set with `-a`). This works for recursively
  searching for `APKINDEX.tar.gz` within the repository path (`-r` or default)
  and using those paths as repositories.
* `remove-autodeps` Remove automatic dependencies possibly installed in the
  build root.
* `zap` Remove the build root.
* `fetch`, `extract`, `patch`, `configure`, `build`, `check`, `install`, `pkg`
  Given an argument of template path (`category/name`) this will invoke the
  build process for the given template up until the given phase. The `pkg`
  phase contains all of the others. For example, `configure` will invoke
  all of `fetch`, `extract`, `patch` and `configure` phases before stopping
  there. A complete `pkg` will also take care of automatically cleaning up
  afterwards, unless overridden. The build will not run if an up to date
  version of the package already exists in the local repository, unless
  overridden with `-f` or `--force`.

<a id="config_file"></a>
### Configuration File

Most options can be specified in the configuration file as well. The system
reads `etc/config.ini` by default (can be changed with `-c`). It follows a
standard `ini` format of Python `configparser`.

There is a sample configuration file in `etc/config.ini.example`. It contains
every option that can be specified, with its default value. You do not need
to specify every option in your own configuration file, this file is only
for reference.

<a id="cross_compiling"></a>
## Cross Compiling

The `cbuild` system is fully capable of cross compiling. The same architecture
profile can be used for both native and cross builds, and in a lot of cases
the process can be entirely transparent.

Unlike native builds, cross builds are not capable of running the `check` phase
so it is always skipped.

Cross compiling is nearly identical to compiling natively. You just need to
do something like this:

```
$ ./cbuild.py -a aarch64 pkg main/zlib
```

The system will automatically take care of setting up an architecture sysroot
within the build root and preparing it for installing `makedepends`. If the
necessary toolchain packages for the cross architecture do not exist, they are
built first. Cross sysroots are persistent, i.e. they are permanently set up
in your build root, but have the same guarantees as the rest of the root, so
once they are set up they should never get corrupt.

<a id="ccache"></a>
## Ccache

The builds will transparently use `ccache` to speed things up if enabled. This
does not apply to `bootstrap`, which never uses the cache.

You can enable this in your `config.ini`, simply by setting `ccache = yes` in
the `build` section. You can also alter the path where the cache files are
stored with `ccache_path = PATH`. See `config.ini.example` for reference.

<a id="help"></a>
## Help

If you still need help, you should be able to get your answers in our
IRC channel (`#chimera-linux` on `irc.oftc.net`) or our Matrix channel
(`#chimera-linux:matrix.org`). The two are linked, so use whichever
you prefer.
