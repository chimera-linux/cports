# cports

Cports is a collection of source package ports for Chimera. The system has been
written specifically for the distribution using the Python scripting language.

Originally started as a rewrite of `xbps-src` from Void Linux, it has since
transitioned to the `apk` packaging system (of Alpine Linux).

Currently it is still very much work in progress.

## TODO

* Currently the system is a work in progress, so the package set is not set in
  stone. Things will likely undergo significant changes.
* Cross-compiling is not yet supported.
* Various commands and flags are currently unimplemented.
* There may be bugs scattered around the place.

## Getting started

Since Chimera does not currently provide binary packages, you'll have to bootstrap
it yourself if you want to test things.

### Requirements

These tools are always needed, regardless of whether bootstrapping or not.

* Python (3.x, any recent version should be okay)
* `scanelf` (from `pax-tools`)
* `apk` (from `apk-tools`)
* `openssl`
* `git` (not mandatory but necessary for reproducible output)
* `bwrap` (from `bubblewrap`)
* `tee`

### Bootstrap prerequisites

You will need a `musl` based system (e.g. Void Linux's `musl` flavor or Alpine Linux)
to start with. Also, you will need the following tools:

* `clang` with `lld`, `libc++`, `compiler-rt` and LLVM's `libunwind`
* `cmake`
* `meson`
* `pkg-config`
* GNU `make` (either as `gmake` or as `make`)
* NetBSD `make` (either as `bmake` or as `make`)
* `ninja`
* `strip`
* `byacc`
* `flex`
* `perl`
* `m4`

You should be able to find them in your host distro's package collection. They are
necessary as binary tools needed to build various packages.

### How it works

The `cbuild` system, similarly to Void's `xbps-src`, builds software in a safe and
minimal container called the `masterdir`. This container is pretty much a `chroot`
style environment (but running unprivileged thanks to `bwrap`) which is used as
a starting point. Dependencies are installed into this container before any
software is built.

There are two kinds of build dependencies, host and target dependencies. When not
cross-compiling, they are the same.

Packages are stored in a local repository within the `hostdir`. The `hostdir` also
contains source distfiles and caches.

The system automatically signs your packages, if a signing key is provided.

### Preparing

First you will need to generate your signing key. You can do that like this:

```
$ ./cbuild.py keygen
```

You can optionally pass your private key name (or path) as an argument. If you do
not, it will be assigned an automatic name consisting of your Git email address
(or system username if unavailable) and a timestamp, plus the `.rsa` extension.
Your public key will be stored in the same location, with the `.pub` extension.

An optional second argument can specify the key size (2048 by default).

The default path for key storage is `etc/keys`.

Once generated, you will receive instructions on how to set up the `cbuild` config
file so it can use the keys.

If you do not create and set up a key, your packages and repo will be unsigned.

### Bootstrap process - stage 0

The bootstrapping process has three stages. The first stage is initiated like this:

```
$ ./cbuild.py bootstrap
```

We call this stage 0. During this stage, host tools (including the compiler) are used
to build a minimal collection of packages (enough to assemble the `masterdir`).

Once this finishes, you will have a `masterdir` present, plus the built packages in
the `hostdir/binpkgs` repository.

While this `masterdir` can be used to build packages right away, you are not supposed
to as it can be influenced by the host configuration.

If the building fails at any stage, you will need to correct the issue (or report a
bug if it's on our side) and issue the command again. It will not build things that
are already built.

### Bootstrap process - stage 1

You can initiate this stage by getting rid of your `hostdir/binpkgs` (but keeping
the `masterdir`) and then issuing a command to build the `masterdir` primary
metapackage, `base-chroot`.

```
$ mv hostdir/binpkgs hostdir/binpkgs_bak
$ ./cbuild.py pkg base-chroot
```

If this completes successfully, kill your old `masterdir` and rebootstrap:

```
$ ./cbuild.py zap
$ ./cbuild.py binary-bootstrap
```

This will use your newly built binary repository to assemble a fresh `masterdir`.

You now have a stage 1 root, which is close to what you want.

### Bootstrap process - stage 2

However, the stage 1 packages were built with a "dirty" toolchain. While it's highly
likely that the packages are already identical to final, it is not guaranteed.

Therefore, just repeat the stage 1 process again, but using your newly built
packages. Once that is done and you've once again zapped your `masterdir` and
reassembled it, you should have a final `chroot` that is ready to build packages.
