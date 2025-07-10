# Using cports

This document provides a comprehensive reference on using the `cports` system,
more specifically its `cbuild` component.

*Table of Contents*

* [Introduction](#introduction)
* [Getting Started](#getting_started)
  * [Requirements](#requirements)
  * [How It Works](#how_it_works)
  * [Preparing](#preparing)
  * [Build Root Setup](#root_setup)
  * [Building a Package](#building_package)
* [Bootstrapping From Source](#bootstrapping)
  * [Bootstrap Requirements](#bootstrap_requirements)
  * [Bootstrap Process](#bootstrap_process)
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
[`Packaging.md`](Packaging.md) instead.

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
`chroot`. At least 2GB of RAM per each CPU thread is recommended (all threads are
used by default).

The `cbuild` tool has relatively few dependencies. You can usually find all of
them in any Linux distribution. Additionally, it imposes some requirements on
the Linux kernel you are running.

The userland dependencies are the following:

* Python 3.12 or newer
* `apk` (from `apk-tools`, static binaries can be obtained [here](https://repo.chimera-linux.org/apk))
* `openssl` (key generation only; not needed otherwise)
* `git`
* `bwrap` (from `bubblewrap`)

If running a Chimera system, these tools can all be installed with the
`base-cbuild-host` metapackage.

**You need a recent Git snapshot of `apk-tools` at this point.** It is your
responsibility to ensure that your `apk` is new enough (`cbuild` does some
rudimentary testing that it's 3.x) and compatible with `cbuild`. Your best
bet is to use the same version as is packaged.

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

You will also want to ensure you have sufficient RAM available. The `cbuild`
system will by default use all CPU threads it can, unless you manually restrict
it.

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
a sandbox with different restrictions depending on the *phase* of the build.

Most of the time, the build root is:

* Read only - after installing dependencies, programs run within are not allowed
  to write outside of their designated directories.
* Without network access - after fetching all sources, programs are not allowed
  to access the network from within. This enforces the policy of having to fetch
  all of their files ahead of time. Checksums are enforced for those files.
* Isolated - the sandbox does not have access to the outside file system.
* Unprivileged - after the `fetch` phase, all namespace types are unshared.

When building a package, the following happens, in simplified terms:

* Build dependencies are installed in the sandbox, provided they are available.
  If some dependency is unavailable, it is built first, using the same process.
  This can happen recursively.
* All declared sources are fetched, if not already cached. They are subsequently
  verified (the checksums must match what the template declares). If this fails,
  the fetch is re-tried.
* Sources are extracted, prepared and patches are applied if necessary.
* The software is configured and built within the sandbox.
* Files are installed in a special `destdir`. Outside of this, the directory
  where files are extracted, the `/tmp` directory in the sandbox and potential
  cache directories (e.g. for `ccache`), the entire sandbox is read only during
  all phases other than `deps` (i.e., after installing dependencies).
* Packages are created in the local repository and signed.

If you are familiar with `xbps-src`, these are the main conceptual differences:

* Most `cbuild` code is run outside the sandbox. Only specific commands are run
  within, which includes dependency installation, sources extraction, patching,
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
  the `-t` flag still exists. Instead of using an overlay, it will bootstrap
  a fresh temporary root. Unlike with `xbps-src`, this does not create a
  performance problem, as everything is much faster.
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
$ ./cbuild keygen
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
packages.

<a id="root_setup"></a>
### Build Root Setup

The easiest way to bring up a build container is from binary packages, like
this:

```
$ ./cbuild bootstrap
```

By default, this will be `bldroot` inside your `cports` directory. If you have
just done a source bootstrap, there is a chance you don't need to run this as
the source bootstrap does it for you as the last step. You will need to do this
if you ever need to re-create it.

If your system has `openssl.cnf` in a non-standard path (i.e. not `/etc/ssl/openssl.cnf`)
and you are using static host `apk`, you can export the `OPENSSL_CONF` envvar
with the actual path if you are getting certificate errors.

<a id="building_package"></a>
### Building a Package

Then, the only thing left to do is to pick a package to build. Let's say,
`apk-tools` from the `main` category. You need to run this:

```
$ ./cbuild pkg main/apk-tools
```

The inverse syntax

```
$ ./cbuild main/apk-tools pkg
```

is also accepted as a special case.

This will parse `main/apk-tools/template.py` and build it according to the
metadata and routines declared in the template.

That's it!

<a id="bootstrapping"></a>
## Bootstrapping From Source

This is an alternative to binary bootstrap, if you wish to compile the whole
system from source. Keep in mind that this takes a long time, because it has
to rebuild the whole bootstrap path 4 times.

Bootstrapping has more requirements than simply using the system. It is also
not guaranteed to work at all times, as we do not check it regularly. Most users
should stick with bootstrapping from packages.

<a id="bootstrap_requirements"></a>
### Bootstrap Requirements

The base requirements of `cbuild` still apply. You also need to be running a
system based on the `musl` C library. This can be for example Void Linux or
Chimera itself. Alpine Linux is not supported for direct bootstrapping because
of its patched musl SONAME (which would be more effort to work around).

The system must contain an initial toolchain. It consists of these:

* `clang` with `lld`, `libc++`, `compiler-rt` and LLVM `libunwind`
* `cmake`
* `meson`
* `patch`
* `pkg-config` (`pkgconf` or the regular one)
* GNU `make` (called `make`)
* `ninja`
* `strip`
* `byacc` or `bison` (either with `yacc` symlink)
* `flex`
* `perl`
* `m4`
* Linux kernel headers for userland usage

These can all be found in most distributions' package collections. If running
a Chimera system, these tools can all be installed with the `base-cbuild-bootstrap`
metapackage.

It is possible to do an almost full source bootstrap on an incompatible system,
provided that Chimera ships binary packages for the given architecture. See
below for an example.

<a id="bootstrap_process"></a>
### Bootstrap Process

Chimera uses a 4-stage bootstrap process. It is largely automatic and hidden
from you. You can invoke it like:

```
$ ./cbuild source-bootstrap
```

Optionally you can stop the process at a specific stage by passing its number
as an argument.

To explain what's going on:

* Stage 0 is software built inside the system you are running.
* Stage 1 is software built inside the system assembled from stage 0.
* Stage 2 is software built inside the system assembled from stage 1.
* Stage 3 is software built inside the system assembled from stage 2.

The initial stage is raw and intentionally stripped down. Its purpose is to
get a minimal environment going, to free further builds of the host system's
influence and narrow down the dependencies. This stage will likely not be
reproducible between different systems.

Stage 1 resembles a final container. Unlike stage 0 build, it uses its own
host tools. The feature set of the packages may not be complete, with some
subpackages (e.g. LLVM debugger) not being built. LTO is also not applied
for this stage yet.

Stage 2 is considered almost final, being built with all of the features of
a final system within a Chimera container, including full LTO. Unit tests
are not run yet as they are not considered reliable.

Stage 3 is the final stage, which is a clean rebuild of every bootstrap
package using a "good" toolchain. There is no distinction from regular
package builds (these are considered stage 3 as well) and unit tests and
so on are run normally.

Templates should in general not make any distinction between stage 2 and 3
builds, as they are to be considered feature-equivalent.

You will have the following artifacts:

* `bldroot-stage0` is the build root that was assembled from packages originally
  built on the host system.
* `bldroot-stage1` is the build root assembled from stage 1 packages.
* `bldroot-stage2` is the build root assembled from stage 2 packages.
* `bldroot` is the final build root; if you remove it and `bootstrap`,
  you will get the same thing.
* `packages-stage0` is the repository of packages `bldroot-stage0` is created
  from.
* `packages-stage1` is the repository of packages `bldroot-stage1` is created
  from.
* `packages-stage2` is the repository of packages `bldroot-stage2` is created
  from.
* `packages` is the final repository.
* `sources` is the sources cache, shared for all.

You can remove all the `*-stage*` directories if you want. They are present
mostly for inspection and possibly debugging.

If the bootstrap fails at any point, you can start it again and it will continue
where it left off. No things already built will be built again.

If you have an incompatible system and wish to do a source bootstrap, you can
run most of the process provided that Chimera already has existing binary
packages for the architecture. In this case, the host system requirements
are identical to regular builds without source bootstrap.

This is done by pre-bootstrapping a stage 0 environment from binaries:

```
$ ./cbuild -b bldroot-stage0 bootstrap
```

Also see the note about certificates in the "Build Root Setup" section.

After that, you can run the `bootstrap` command as usual. The stage 0 will be
skipped (but it's largely unnecessary due to the environment already being
a Chimera environment and not dependent on host toolchain) but every other
stage will build.

<a id="cbuild_reference"></a>
## Cbuild Reference

Every `cbuild` action consists of the following:

```
$ ./cbuild [optional arguments] COMMAND [command arguments]
```

For commands that take a package name (i.e. a slash is present in the arg),
you can also swap the order:

```
$ ./cbuild [optional arguments] PACKAGE COMMAND [additional arguments]
```

This is a minor convenience feature as in "perform action on package".

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

* `-A ARCH`, `--host-arch ARCH` Override the host architecture. The given host
  arch must be runnable on the current kernel. This is typically useful for e.g.
  32-bit builds on 64-bit architectures, or for emulated targets. Note that once
  a build root is bootstrapped, it decides the host architecture exclusively, so
  this is mostly useful for actions that bootstrap a new root.
* `-a ARCH`, `--arch ARCH` Build for architecture `ARCH`, possibly cross compiling.
* `-b ROOT`, `--build-root ROOT` *(default: `bldroot`)* Set the path to the build
  root to use.
* `-B PATH`, `--build-dir PATH` *(default: empty)* Set the path to the directory
  where builds will happen. If not set, `builddir` inside the build root will be
  used as is. Otherwise, it will be bound to the given path (which will be created
  if necessary).
* `--bulk-continue` When doing bulk builds, do not abort the whole bulk if a
  package fails. This may result in incorrect build order.
* `-c PATH`, `--config PATH` *(default: `etc/config.ini`)* The path to the config
  file that `cbuild` reads configuration data from. If relative, it is to cports.
* `-C`, `--skip-check` Never attempt to run the `check` phase.
* `-D`, `--dirty-build` Skip installation of dependencies in the `bldroot`,
  as well as removal of automatic dependencies after successful build, and
  do not clean the remains of a previous build of the template from `builddir`
  and `destdir`. This is mostly useful to continue previous failed builds.
  For `chroot`, it skips repository index refresh.
* `--dry-run` Do not perform any changes on the file system. This applies to only
  specific commands, notably the `prune-` commands.
* `-f`, `--force` Packages will be created and overwritten even if one already
  exists in the local repository.
* `-G`, `--no-dbg` Do not build `-dbg` packages.
* `-j JOBS`, `--jobs JOBS` *(default: thread count)* The number of build jobs to
  use. By default uses the number of CPUs the cbuild run is restricted to (which
  is usually the number of CPU threads you have). If you have insufficient RAM
  (at least 2GB per thread is recommended), you will want to lower this. Setting
  to 0 uses the default.
* `-K`, `--keep-temporary` Keep temporary build files after a successful build,
  this includes the `builddir` and `destdir`. If using a temporary build root,
  it will not be removed.
* `-L`, `--no-color` Color output will be suppressed. By default color output
  is used, unless `NO_COLOR` is set in the environment or the output is being
  redirected/piped.
* `--no-depends-check` Skip checking availability of host/makedepends with
  the same version as the template in the repository. Instead, the packages
  are simply installed from the repository regardless of version. Runtime
  dependency availability checks are skipped. This mode is potentially
  unsafe and should not be used most of the time, but can be used e.g. when
  locally building a package with build dependencies that are still being
  built on remote builders to avoid `cbuild` rebuilding them without having
  to revert the versions in the templates.
* `-N`, `--no-remote` Never use remote repositories to fetch dependencies.
* `-r REPO`, `--repository-path REPO` *(default: `packages`)* Set the path to the
  local repository to build packages in.
* `-R REPO`, `--alt-repository REPO` *(default: None)* Create packages into an
  alternative repository. This is a completely separate repository path. When
  installing dependencies, both repositories are considered; when checking for
  whether to build at all, only the alternative repository is considered. This
  is useful for doing various quick tests and so on without messing up your
  main repo, while still pulling build dependencies from the primary one.
* `-s SOURCES`, `--sources-path SOURCES` *(default: `sources`)* Set the path to the
  sources cache.
* `--stage` Keep newly built packages staged. They will get unstaged either with
  the next build or by explicitly doing so.
* `--stage-path REPO` *(default: `pkgstage`)* Packages are staged into a separate
  location before being migrated into the primary repository. This separate location
  mirrors the primary repository's layout. This allows one to "hide" changes until
  they are ready, for example until all shlibs are properly bumped.
* `--status-fd N` A file descriptor number (must be open) to be used for status
  reporting in bulk builds.
* `-t`, `--temporary` Create a temporary `bldroot` for the build. The `-b` argument
  is used as a base path as well as the name prefix for the temporary root if
  provided. The temporary root is removed at the end (whether the build succeeded
  or failed) unless `--keep-temporary` is passed.
* `--update-check` Do not permit a build for a template that has broken update
  checking or has newer versions available.

<a id="commands"></a>
### Commands

The following commands are recognized:

* `bootstrap` Create a build root from packages. The local repository must
  be populated, or a sufficient remote repository must be available. An older
  alias `binary-bootstrap` is available as well.
* `bootstrap-update` Update the packages in your build root to latest.
  Acts like `binary-bootstrap` if the `bldroot` does not exist.
* `bulk-pkg` Given a list of bulk expressions (may be zero, see below), perform
  a bulk build. The templates are sorted topologically, accounting for any
  intermediate deps so that the build order is always guaranteed correct.
  A status file descriptor (`--status-fd`) may be given, in which case
  the final status of each template's build is written on a new line, in the
  format `NAME STATUS`. The `STATUS` may be `skipped` (if skipped because of
  previous failure), `invalid` (if an invalid template is given), `missing`
  (if the template is a valid name but it's not found), `parse` (if it was
  found but failed to parse), `broken` (if it's explicitly marked `broken`),
  `failed` (if it failed to build) or `ok`. The bulk expressions themselves
  may be a variety of things; if given no expressions, a full bulk build of
  the whole `cports` is performed, otherwise the inputs may be simple template
  names (like for `pkg`), category names (e.g. `main`), or special expressions.
  The special expressions include `list:XXX` (a list of template names separated
  by whitespace, but given as a single string), `file:PATH` (a file containing
  a list of bulk expressions each on a new line), `-` or `file:-` (expressions
  are collected from `stdin`), `status:unbuilt` (all templates that are not
  built in a local repo), `status:outdated` (all templates that are built
  locally but not up to date), `status:FILE` (given a status file emitted by
  `--status-fd` in a previous bulk, build those that were skipped or failed to
  build; broken/invalid/missing/built templates are not included), or `git:EXPR`
  (templates affected by the given Git expression; this may be a single commit
  or a range of commits (`A..B`, half-open interval like regular Git ranges),
  the commit may be represented by a name (e.g. branch name, `HEAD` and others,
  just like in Git) and may include a positive or negative commit message `grep`
  (e.g. `git:COMMIT+GREP` where `GREP` may be optionally prefixed with `^`,
  which makes the expression case-insensitive, and `!`, which makes the match
  negative).
* `bulk-print` Like `bulk-pkg`, but only print the template names instead of
  building them. The status reporting still works but obviously won't include
  build failures, only parse failures and the likes.
* `bulk-print-ver` Like `bulk-print`, but include the version in the listing
  like `pkgname=pkgver-rN`.
* `bulk-raw` Perform a raw bulk build. In this mode, only template names may
  be given, no special expressions, and no sorting is done, i.e. packages are
  built in the order that is given.
* `bump-pkgrel` Given a list of template names (at least one), increase
  the `pkgrel` number by one for each.
* `bump-pkgver` Given a template name and a valid apk version, update the
  `pkgver` of the template to that version.
* `chroot` Enter the build root with an interactive shell. In this environment,
  the root is mostly unsandboxed, i.e. writable and with network access. You
  can use this kind of environment for quick testing, as well as entering failed
  builds and inspecting them. By default it starts in `/tmp` but you can also
  pass a template name and then it will start inside the template's build
  directory if it exists (or `/builddir` if not).
* `clean` Clean up the build root. This means removing automatic dependencies
  and removing `builddir` and `destdir` within. When given a template name,
  it will only clean the directories for that template.
* `commit` Commit a given template or templates. Currently, only individual
  templates are supported, and one commit will be generated for each. Any
  optional arguments after `--` will be passed to `git commit` directly.
* `cycle-check` Scan all templates or a single template for build-time
  dependency cycles. Only one cycle at a time is printed. The goal is to
  keep the tree free of cycles at all times. Therefore, if you encounter
  a cycle, resolve it and check again.
* `dump` Dump serialized template metadata in JSON format for all of `cports`.
* `deps`, `fetch`, `extract`, `prepare`, `patch`, `configure`, `build`, `check`,
  `install`, `pkg` Given an argument of template path (`category/name`) this
  will invoke the build process for the given template up until the given phase.
  The `pkg` phase contains all of the others. For example, `configure` will
  invoke all of `fetch`, `extract`, `prepare`, `patch` and `configure` phases
  before stopping there. A complete `pkg` will also take care of automatically
  cleaning up afterwards, unless overridden. The build will not run if an up to
  date version of the package already exists in the local repository, unless
  overridden with `-f` or `--force`, when using the "pkg" target. Other
  targets will run always unless already finished in builddir (you can
  make them always run regardless by passing `-f` or `--force`). Passing
  multiple packages to `pkg` is a special case and is an alias for `bulk-pkg`.
* `index` When not given a path, reindex all known repositories. When given
  a path, reindex a specific repository. Only either the host architecture or
  the `-a` architecture are indexed, and the path should not include the
  architecture.
* `interactive` Enter a prompt where `cbuild` commands can be entered.
  They take the same syntax as always, just without explicitly calling `cbuild`.
* `invoke-custom` Takes a target name and a package. Invokes a custom-defined
  template-specific target function. Typically used to handle logic for
  generation of bootstrap bindists, kernel config refresh, and the likes.
* `keygen [PREFIX [KEYSIZE]]` Generate your signing key. You can optionally
  specify the prefix (typically an email) and key size (2048 by default).
  The configuration file will automatically be updated if no existing setting
  is present. If an existing setting is present and you don't specify anything
  on command line and there is no pre-existing key, it will be generated. The
  system will not overwrite keys that already exist (i.e. if a valid key is
  specified in configuration, this will fail).
* `lint` Read and parse the template, and do lint checks on it. Do nothing
  else. Error on failures.
* `prepare-upgrade` Given a template name (one), read the template, fetch its
  sources, update the `sha256` fields appropriately to match what was
  downloaded, and reset `pkgrel` to zero. Note that you still need to manually
  check whether the downloaded sources are good, don't trust it blindly.
* `print-build-graph` Given a template name, print the build graph like if the
  repository was empty, accounting for dependencies. Each further build level
  (i.e. when a template is built as a dependency of another) is indented by
  an extra space. Otherwise, the template names are printed on their own lines.
* `prune-pkgs` Like running `prune-obsolete` followed by `prune-removed`.
* `prune-obsolete` Prune obsolete packages within all repositories for the
  current architecture (can be set with `-a`). This works for recursively
  searching for `APKINDEX.tar.gz` within the repository path (`-r` or default)
  and using those paths as repositories.
* `prune-removed` Prune removed packages within all repositories for the
  current architecture (can be set with `-a`). This works for recursively
  searching for `APKINDEX.tar.gz` within the repository path (`-r` or default)
  and using those paths as repositories. The affected repositories are
  reindexed afterwards.
* `prune-sources` Given no arguments, clean up the `sources/`. That includes
  removing any sources that are no longer referred to by any template, as well
  as any other unrelated files.
* `relink-subpkgs` Recreate subpackage symlinks for a template. If not
  given any arguments, it will do it for all available templates. Otherwise,
  it will do it for the given template. Invalid symlinks will be deleted
  when the global action is performed, otherwise symlinks will only be
  created or replaced. For the global action, passing `prune` as an
  argument will result in the command also removing invalid directories
  (not containing templates) and files.
* `remove-autodeps` Remove automatic dependencies possibly installed in the
  build root.
* `source-bootstrap [STAGE]` Bootstrap from source. If `STAGE` is passed, stop
  at that stage (number). By default, that is `2`. Stage 0 bootstrap must be
  run in a compatible host system.
* `unstage` Attempt unstaging the repositories if possible. If conflicts
  prevent it from doing so (i.e. missing rebuilds and so on) you will get
  a warning instead, and nothing will happen. Warnings will result in
  return code 32, success is 0, other values are a failure.
* `unstage-check-remote` Treating the local repository as a stage, check
  if the local packages would unstage cleanly in the remote repo. This is
  useful to check if you've missed some rebuilds locally when rebuilding
  for changed SONAMEs and so on.
* `update-check` Check the given template for new versions. An extra argument
  (may be any) makes the output verbose. See the relevant section inside the
  packaging manual.
* `zap` Remove the build root.

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
$ ./cbuild -a aarch64 pkg main/zlib
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

You can enable this in your `config.ini` by setting `ccache = yes` in the
`build` section. The cache will be stored in the `ccache` subdirectory of the
cbuild caches path (by default `cbuild_cache`, see `config.ini.example` for how
to change it).

<a id="help"></a>
## Help

If you still need help, you should be able to get your answers in our
IRC channel (`#chimera-linux` on `irc.oftc.net`) or our Matrix channel
(`#chimera-linux:matrix.org`). The two are linked, so use whichever
you prefer.
