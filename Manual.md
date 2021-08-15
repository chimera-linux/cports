# The Chimera Linux packaging manual

This manual is supposed to provide a comprehensive reference for Chimera Linux
packaging, i.e. a comprehensive reference for the packaging format.

In general, things not described in the manual are not a part of the API and
you should not rely on them or expect them to be stable.

*Table of Contents*

* [Introduction](#introduction)
  * [Categories](#categories)
  * [Quality Requirements](#quality_requirements)
  * [Build Phases](#phases)
  * [Template Naming](#naming)
* [Contributing](#contributing)
* [Help](#help)

<a id="introduction"></a>
## Introduction

This repository contains both the `cbuild` program (which is used to build
packages) as well as all the packaging templates. The templates are basically
recipes describing how a package is built.

The `cbuild` program is written in Python. Likewise, the packaging templates
are also written in Python, being special scripts containing metadata as well
as functions that define the build steps.

For usage of `cbuild`, see the `README.md` file in this repository. The manual
does not aim to provide usage instructions for `cbuild`.

The `cbuild` program provides infrastructure, which allows the packaging
templates to be simplified and often contain only a few fields, without having
to contain any actual functions. For example:

```
pkgname = "foo"
version = "0.99.0"
revision = 0
build_style = "gnu_makefile"
short_desc = "A simple package"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
homepage = "https://foo.software"
distfiles = [f"https://foo.software/{pkgname}-{version}.tar.gz"]
checksum = ["ad031c86b23ed776697f77f1a3348cd7129835965d4ee9966bc50e65c97703e8"]
```

Of course, often a template will be a lot more complicated than this, as
packages have dependencies, build systems are not always standard and so on.

The template is stored as `template.py` in one of the packaging categories,
in a directory named the same as `pkgname`. That means for this example it
may be `main/foo/template.py`.

The `cbuild` program can read templates and build packages according to the
metadata and functions stored. This happens in a special container environment
which is controlled and highly restricted.

You can invoke `cbuild` to build the software like this:

```
$ ./cbuild.py pkg main/foo
```

The result will be a local repository containing the binary packages.

<a id="categories"></a>
### Categories

The Chimera packaging collection provides four categories in which templates
can go. These currently are:

* `main`
* `contrib`
* `non-free`
* `experimental`

Each category has its own repository that is named the same as the category.

The `main` category contains software curated and supported by the distro.
In general, a system composed purely of `main` packages should be bootable,
but may not contain all functionality required by users. Templates are
evaluated for `main` based on various factors such as usefulness, quality of
the software, licensing and others. Teplates in `main` must not depend on
templates in other categories.

The `contrib` category is a *user repository*. The requirements for `contrib`
are looser than for `main` and the software is not officially supported by
the distribution, but the distro still provides hosting for binary packages
and templates undergo review and acceptance by the distro maintainers. In
addition to other `contrib` templates, software here may depend on `main`
templates.

The `non-free` category in general contains proprietary software and stuff
that we cannot redistribute. Software here may depend on anything from `main`
or `contrib`. Unlike `contrib` packages, no binary packages are shipped and
users need to build it themselves.

Finally, the `experimental` category is a mostly unrestricted and has the
least stringent quality requirements. Anything that is anyhow controversial
goes here; once determined to be acceptable, a maintainer may move the
template to `contrib` (or sometimes `non-free`). Software in this category
does not have binary packages shipped and users are on their own testing it.

<a id="quality_requirements"></a>
### Quality Requirements

In order to be included in `experimental`, there are few requirements. The
software has to provide something of usefulness to the users and must not
be malicious. At the time of introduction, it must satisfy the general style
requirements and must be buildable.

For inclusion into `contrib`, the software must additionally be provided
under a redistributable license and must be open source; when possible, it
must be packaged from source code (there may be exceptions, but they are
rare, such as bootstrap toolchains for languages that cannot be bootstrapped
purely from source code).

Inclusion into `main` requires the software to work on all tier 1 targets.
Additionally, it has to not be vetoed by any core reviewer. In general,
unless there is a good reason for inclusion into `main`, things shall
remain in `contrib`.

Templates seeking introduction into `contrib` or better should in general
be packaged from stable versions. That means using proper release tarballs
rather than arbitrary `git` or similar revisions. Exceptions to this may
be made for `contrib` (such as when the software is high profile and the
latest stable release is very old and provides worse user experience) but
not for `main`.

<a id="phases"></a>
### Build Phases

Building a package consists of several phases. All phases other after `setup`
until and including `install`  can have template specified behavior. The build
system itself runs outside of the sandboxed container, while most actions
(such as building) run inside.

Except for the `setup` and `fetch` phases, the build system is configured
to unshare all namespaces when performing actions within the sandbox. That
means sandbox-run actions have no access to the network, by design.

Except for the `setup` phase, the sandbox is mounted read only with the
exception of the `builddir` (before `install`), `destdir` (after `build`)
and `tmp` directories. That means once `setup` is done, nothing is allowed
to modify the container.

All steps are meant to be repeatable and atomic. That means if the step
fails in the middle, it should be considered unfinished and should not
influence repeated runs. The build system keeps track of the steps and
upon successful completion, the step is not run again (e.g. when the
build fails elsewhere and needs to be restarted).

* `setup` The build system prepares the environment. This means creating
  the necessary files and directories for the syndbox and installing the
  build dependencies. When cross-compiling, the cross target environment
  is prepared and target dependencies are installed in it.

* `fetch` During `fetch`, required files are downloaded as defined by the
  `distfiles` metadata variable by default (or the `do_fetch` function of
  the template in rare cases). The builtin download behavior runs outside
  of the sandbox as pure Python code. When overridden with `do_fetch`, it
  also overlaps with the `extract` stage as the function is supposed to
  prepare the `builddir` like `extract` would.

* `extract` All defined `distfiles` are extracted. The builtin behavior
  runs inside of the sandbox, except when bootstrapping.

* `patch` This phase applies patches provided in `templatedir/patches`
  to the extracted sources by default. User defined override can perform
  arbitrary actions.

* `configure` In general this means running the `configure` script for the
  software or something equivalent, i.e. prepare the software for building
  but without actually building it.

* `build` The software is built, but not installed. Things run inside of
  the sandbox are not expected to touch `destdir` yet.

* `check` The software's test suite is run, if defined. By default tests
  are run (except when impossible, like in cross builds). It is possible
  to turn off tests with a flag to `cbuild`, and templates may disable
  running tests.

* `install` Install the files into `destdir`. Well behaved templates are
  not supposed to change the `builddir` anymore, so by default it will
  be mounted read-only at this point. However, this is overridable since
  there is software that cannot be convinced; this should be used very
  sparingly in general though. If the template defines subpackages,
  they can define which files they are supposed to contain; this is
  done by "taking" files from the initial populated `destdir` after
  the template-defined `do_install` finishes.

* `pkg` Create binary packages and register them into your local repo.

* `clean` Clean up the `builddir` and `destdir`.

When building packages with `cbuild`, you can invoke only the specific
phase (from `fetch` to `pkg`). All phases leading up to the specified
phase are run first, unless already ran.

<a id="naming"></a>
### Template Naming

<a id="contributing"></a>
## Contributing

If you want to contribute, you need to take the following steps:

1) Fork the `cports` repository
2) Read `CONTRIBUTING.md`
3) Work on your contribution, ensuring quality requirements are met
   (if you are unsure, do not hesitate to ask for help)
4) Create a pull request with the changes
5) Wait for a review or merge; if the changes are clean, they may get
   merged right away, otherwise you will be asked to make changes

<a id="help"></a>
## Help

If you still need help, you should be able to get your answers in our
IRC channel (`#chimera-linux` on `irc.oftc.net`) or our Matrix channel
(`#chimera-linux:matrix.org`). The two are linked, so use whichever
you prefer.
