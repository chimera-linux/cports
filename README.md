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

### Bootstrap process

To perform a full bootstrap, simply run the following:

```
$ ./cbuild.py bootstrap
```

You can also stop the bootstrap process at a specific stage by passing the
stage number (0, 1 or 2) as an argument after `bootstrap`. To explain what
is going on, read below.

#### Bootstrap process - stage 0

The bootstrapping process has three stages. First is stage 0, which is built
on the host system (without any isolation). Your host system is used to build
a minimal set of packages required to assemble the `masterdir`.

Once the first stage completes, you should have a `masterdir-stage0` (assembled
container) as well as `hostdir/binpkgs-stage0` (built package repository).

This `masterdir` is enough to build software, but you are not supposed to use it
directly since it is largely influenced by the host software and configuration.

If the building fails at any stage, you can just restart it and it will continue
where it left off. It will not build any things already built.

### Bootstrap process - stage 1

Once a stage 0 `masterdir` is available, this stage will proceed. It will generate
a `masterdir-stage1` as well as `hostdir/binpkgs-stage1`.

This `masterdir` is fairly close to the actual final container, but may still
contain leftovers caused by the toolchain used to build it being "dirty". That
is why everything needs to be rebuilt once again.

### Bootstrap process - stage 2

Once a stage 1 `masterdir` is available, this stage is built. It is built in exactly
the same way as stage 1, except it will create a `masterdir` and its repository
will be stored in `hostdir/binpkgs`.

After the whole process is done, you will have three `masterdirs`, as well as three
repositories. You can discard the first two stages if you want. They are kept around
for reference.

Keep in mind that the `masterdir` as well as `hostdir` path/name may change
based on the configuration file and command line options you pass. The `-stage0`
and `-stage1` suffixes are appended universally though.
