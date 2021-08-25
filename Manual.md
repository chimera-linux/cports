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
  * [Package Naming](#naming)
  * [Filesystem Structure](#filesystem_structure)
  * [Template Structure](#template_structure)
    * [Template Variables](#template_variables)
    * [Template Functions](#template_functions)
    * [Build Styles](#build_styles)
    * [Subpackages](#subpackages)
    * [Template Options](#template_options)
    * [Hardening Options](#hardening_options)
    * [Tools](#tools)
  * [Build Profiles](#build_profiles)
  * [Build Environment](#build_environment)
  * [Hooks and Invocation](#hooks)
* [Template API](#template_api)
  * [Builtins](#api_builtins)
  * [Handle API](#api_handle)
    * [Package Class](#class_package)
    * [Template Class](#class_template)
    * [Subpackage Class](#class_subpackage)
  * [Utility API](#api_util)
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
the software, licensing and others. Templates in `main` must not depend on
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

Finally, the `experimental` category is mostly unrestricted and has the
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
exception of the `builddir` (up to and including `install`), `destdir`
(after `build`) and `tmp` directories. That means once `setup` is done,
nothing is allowed to modify the container.

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
  `distfiles` template variable by default (or the `do_fetch` function of
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

* `install` Install the files into `destdir`. If the template defines
  subpackages, they can define which files they are supposed to contain;
  this is done by "taking" files from the initial populated `destdir`
  after the template-defined `do_install` finishes. At the time the
  subpackages are populated, `builddir` is read-only in the sandbox.
  Ideally it would also be read-only during `install`, but that is
  not actually possible to ensure (since build systems like to touch
  their metadata and so on).

* `pkg` Create binary packages and register them into your local repo.

* `clean` Clean up the `builddir` and `destdir`.

When building packages with `cbuild`, you can invoke only the specific
phase (from `fetch` to `pkg`). All phases leading up to the specified
phase are run first, unless already ran.

<a id="naming"></a>
### Package Naming

All packages should only use lowercase characters that are in the ASCII,
never mixed case, regardless of what the software is called.

In general, the primary package of the template (i.e. not a subpackage)
should follow the upstream name (other than case) regardless of the
contents of the package. That is, when a library is called `foo`,
the package should be called `foo`, not `libfoo`.

However, if a library is a subpackage of a bigger software project,
the `lib` prefix should be used. So if project `foo` consists of a
primary `foo` package and a library subpackage, that subpackage should
be called `libfoo`.

Development packages should use the `-devel` suffix, like `foo-devel`
for the `foo` template. In general, libraries should always have a
corresponding `-devel` package, except in some rare cases where this
does not make sense (primarily development toolchains where the
primary package is already a development package and the library
is split out to avoid installing the whole thing in case of runtime
dependencies).

Development packages should contain `.so` symlinks (where not required
at runtime) as well as include files, `pkg-config` files and any other
files required for development but not required at runtime.

Debug packages have the `-dbg` suffix and are created automatically in
most cases.

If a primary package (typically a library or some kind of module) has
auxiliary programs that are separated into a subpackage, the subpackage
should be called `foo-progs`.

Subpackages for language bindings should put the language name in the
suffix, e.g. `foo-python`. However, language modules that are the primary
package should put that in the prefix, e.g. `python-foo`.

<a id="filesystem_structure"></a>
### Filesystem Structure

Programs meant to be executed directly by the user always go in `/usr/bin`.
The `/usr/sbin`, `/bin` and `/sbin` paths are just symbolic links to the
primary `/usr/bin` path and should never be present in packages.

Libraries go in `/usr/lib`. Do not use `/usr/lib64` or `/usr/lib32`,
these should never be present in packages. Same goes for the toplevel
`/lib` or `/lib64` or `/lib32` paths. In general, compatibility symlinks
are present in the system and they all point to just `/usr/lib`.

Executable programs that are internal and not meant to be run by the
user go in `/usr/libexec` (unless the software does not allow this).

Include files go in `/usr/include`. Data files go in `/usr/share`; the
directory must not contain any ELF executables.

In general, the `/usr` directory should be considered immutable when
it comes to user interventions, i.e. editable configuration files should
not be installed in there. However, non-editable configuration files
should always go there and not in `/etc`.

Editable configuration files go in `/etc`.

Cross-compiling sysroots are in `/usr/<triplet>` where triplet is for
example `powerpc64-linux-musl` (i.e. short triplet). These contain a
simplified filesystem layout (the `usr` directory with the usual files
and symlinks, and the `bin`, `lib` etc symlinks at top level).

<a id="template_structure"></a>
### Template Structure

A template consists of **variables** and **functions**. A simple template
may only consist of variables, while those that need to define some
custom behavior may also contain functions.

The template follows the standard Python syntax. Variables are assigned
like `foo = value`. Functions are defined like `def function(): ...`.

<a id="template_variables"></a>
#### Template Variables

In general, changes made to toplevel variables from inside functions are
not respected as variables are read and stored before the functions are
executed. Any later accesses to variables must be done through the template
handle passed to functions as the first argument (typically called `self`).

These variables are mandatory:

* `pkgname` *(str)* The primary package name, must match template name.
* `version` *(str)* The package version, applies to all subpackages. Must
  follow the correct format for the `apk` package manager.
* `revision` *(int)* The revision number for the package. When changes are
  made to the template that require rebuilding of the package, the revision
  is incremented by one. The initial value should be zero.
* `short_desc` *(str)* A short, one line description of the package. Should
  be kept at 72 characters or shorter. In general, this should not begin with
  an article (`the` is sometimes permissible), and should not end with a period.
* `homepage` *(str)* The homepage URL of the project being packaged. Should
  not include the trailing slash.
* `license` *(str)* The license of the project in SPDX format (e.g.
  `BSD-3-Clause`). If there are multiple licenses, they should be separated
  by a comma and a space (`GPL-2.0-or-later, MIT`).

There is also a variety of variables that are builtin but not mandatory.
Keep in mind that default values may be overridden by build styles.

* `CFLAGS` *(list)* Compiler flags used for the C compiler, regardless of
  profile, at any point. Passed after other compiler flags.
* `CXXFLAGS` *(list)* Compiler flags used for the C++ compiler, regardless of
  profile, at any point. Passed after other compiler flags.
* `FFLAGS` *(list)* Compiler flags used for the Fortran compiler, regardless of
  profile, at any point. Passed after other compiler flags.
* `LDFLAGS` *(list)* Linker flags used regardless of build profile, passed
  after other linker flags.
* `archs` *(str)* A space delimited list of architectures the template builds
  for. May contain wildcards. The `~foo` syntax is a negation.
* `broken` *(str)* If specified, the package will refuse to build. The value
  is a string that contains the reason why the package does not build.
* `build_style` *(str)* The build style used for the template. See the
  section about build styles for more details.
* `build_wrksrc` *(str)* A subpath within `wrksrc` that is assumed to be the
  current working directory during `configure` and later.
* `checksum` *(list)* A list of SHA256 checksums specified as digest strings
  corresponding to each field in `distfiles`. Used for verification.
* `create_wrksrc` *(boolean)* If specified, `wrksrc` is created and the
  `distfiles` are extracted into it rather than into `builddir` directly.
  This is mainly useful when the source tarball does not contain the directory
  but rather its contents.
* `configure_args` *(list)* This list is generally specific to the build
  system the template uses. Generally speaking, it provides the arguments
  passed to some kind of `configure` script.
* `configure_script` *(str)* The name of the script relative to current
  working directory used for configuration. Only used by build styles that
  use such scripts. The default value is `configure`.
* `depends` *(list)* Runtime dependencies of the package. They are not
  installed in the build container, but are checked for availability (and
  built if missing). While these may be just names, you can also specify
  constraints (e.g. `foo<=1.0-r1`) and conflicts (`!foo`).
* `distfiles` *(list)* A list of URLs to download and extract (by default).
  The items can be either strings (in which case the filename is inferred
  from the URL itself) or 2-tuples (in which case the first field is the URL
  and the second field is the file name it will have when downloaded).
* `env` *(dict)* Environment variables to be exported when running commands
  within the sandbox. This is considered last, so it overrides any possible
  values that may be exported by other means. Use sparingly.
* `hardening` *(list)* Hardening options to be enabled or disabled for the
  template. Refer to the hardening section for more information. This is
  a simple list of strings that works similarly to `options`, with `!`
  disabling the hardening options.
* `hostmakedepends` *(list)* A list of strings specifying package names to
  be installed in the build container before building. These are always
  installed in the build container itself rather than target sysroot,
  even if cross compiling. Typically contains runnable tools.
* `maintainer` *(str)* This one is not mandatory but is highly recommended.
  A template with no `maintainer` field is orphaned. No package in the
  `main` section of the `cports` collection must be orphaned.
* `make_cmd` *(str)* The name of the program used for building. May not
  apply to all templates or build styles. By default this is `bmake` (the
  default Make implementation in Chimera).
* `make_build_args` *(list)* A list of custom arguments passed to `make_cmd`
  during build phase.
* `make_build_target` *(str)* The `make_cmd` target to be used to build.
  Different build systems may use this differently. Empty by default.
* `make_install_args` *(list)* A list of custom arguments passed to `make_cmd`
  when installing.
* `make_install_target` *(str)* The `make_cmd` target to be used to install.
  Different build systems may use this differently (`install` by default).
* `makedepends` *(list)* A list of strings specifying package names to be
  installed in the build container. When cross compiling, these are installed
  into the target architecture sysroot. When not cross compiling, this is
  simply concatenated with `hostmakedepends`.
* `nopie_files` *(list)* A list of glob patterns (strings). By default,
  the system will reject non-PIE executables when PIE is enabled, but
  if the file's path matches any of the patterns in this list, it will
  be ignored instead.
* `nostrip_files` *(list)* A list of glob patterns (strings). When scanning
  files to be stripped of debug symbols, each pattern in this list is
  considered. If anything is matched, the file will not be stripped.
  This is useful if you want the default strip behavior for most things
  but there are some files that absolutely cannot be stripped.
* `options` *(list)* Various boolean toggles for the template. It is a list
  of strings; a string `foo` toggles the option on, while `!foo` does the
  opposite. Every permissible option has a default.
* `patch_args` *(str)* Options passed to `patch` when applying patches.
  By default, patches are applied with `-Np1`.
* `provides` *(list)* A list of packages provided virtually, specified
  in the format `foo=1.0-r0`. The package manager will consider these
  alternative names for the package, and automatically have them
  conflict with other packages of this name. If the version part is
  not provided, several packages of that name may be installed, but
  none of them will be considered by default; instead, an error message
  will be given and the user will need to choose.
* `shlib_provides` *(list)* Extra shared libraries to be provided by
  the package. The fields should be 2-tuples; the first element should
  be the `soname`, the second field the full suffix after `.so` (so
  e.g. for file `libfoo.so.1.4.2` with `soname` `libfoo.so.1`, this
  should be `("libfoo.so.1", "1.4.2")`). If there is no suffix after
  the `.so`, you should use the value `"0"`. If there is no `soname`,
  you should use the unsuffixed filename (i.e. `libfoo.so`). Typically,
  you will not use this as the shared library scanning is automatic; but
  sometimes libraries provide either a non-conforming `SONAME` which the
  scanner does not pick up, or the scanner is disabled explicitly.
* `shlib_requires` *(list)* A list of extra shared library dependencies
  for the package. The values should be the `sonames`, not full filenames.
* `skip_extraction` *(list)* A list of filenames in `distfiles` to not
  extract during the `extract` phase.
* `skiprdeps` *(list)* A list of paths (relative to `destdir`) referring
  to files that will not be scanned for runtime dependencies.
* `subpackages` *(list)* A list of subpackages the template provides. The
  list must contain two-tuples of subpackage name and a function defining
  the subpackage. In most cases, you do not need to specify this explicitly.
  See the section about subpackages for more details.
* `tools` *(dict)* This can be used to override default tools. Refer to the
  section about tools for more information.
* `triggers` *(list)* A list of paths the package should trigger on. I.e.
  if any package changes anything in those paths, the trigger script for
  this package should run.
* `wrksrc` *(str)* The working directory the build system will assume
  once distfiles have been extracted (i.e. for `patch` and later, from
  `configure` onwards it may be `build_wrksrc`). By default this is
  `{pkgname}-{version}`.

<a id="template_functions"></a>
#### Template Functions

The other thing template files can specify is functions. Functions define
template logic; they are here for everything that cannot be done in a purely
declarative manner. Functions and variables interact; variables provide data
for the functions to read.

In general, the functions defined by templates are phase functions; they are
associated with a specific build phase. There are some functions that do not
fit this mold, however.

Every user-defined function in a template takes one argument, typically called
`self`. It refers to the template object; you can read the current state of
template variables as well as other special variables through it, and perform
various actions using the API it defines.

The first template-defined function that is called is `init`. This function
is called very early during initialization of the template object; most of
its fields are not populated at this point. The following is guaranteed
during the time `init(self)` is called:

1) Template variables are populated; every template variable is accessible
   through `self`.
2) Template options are initialized.
3) The `build_style`, if used, is initialized.
4) Version and architecture are validated.

The following is guaranteed not to be initialized:

1) Build-style specific template variables are not populated.
2) Build-style specific template variable defaults are not set.
3) Template functions are not filled in.
4) Path variables are not filled in.
5) It is yet unknown whether the build will proceed, since `broken`
   and other things have not yet been checked.
6) Subpackages are not populated.
7) Tools are not handled yet.
8) Mostly everything else.

Basically, you can consider this function as the continuation of global
scope; you can finish any initialization that you haven't done globally
here, before other things are checked.

Assuming the build proceeds, phase functions are called. Every phase may
use up to 4 functions - `init_PHASE`, `pre_PHASE`, `do_PHASE` and `post_PHASE`.
They are called in that order. The `pre_` and `post_` functions exist so that
the template can specify additional logic for when the `do_` function is
already defined by a `build_style`.

The `init_` prefixed function is, unlike the other 3, not subject to stamp
checking. That means it is called every time, even during repeated builds,
which is useful as the template handle is persistent - once data is written
in it, it will last all the way to the end, so you can use the `init_` hooks
to initialize data that later phases depend on, even if the phase itself is
not invoked during this run (e.g. when re-running build after a failure).

The phases for which all this applies are `fetch`, `patch`, `extract`,
`configure`, `build`, `check` and `install`. They are invoked in this
order.

Additionally, the template may also define `pre_pkg`, which is special;
it is not called only for the template handle but rather for every
subpackage as well.

Every other function defined in template scope is not used by `cbuild`.
However, all regular names are reserved for future expansion. If you want
to define custom functions (e.g. helpers) in template scope, prefix their
names with an underscore.

Also keep in mind that the order of execution also interacts with hooks.
See the section on hooks for more information.

<a id="build_styles"></a>
#### Build Styles

Build styles are a way to simplify the template by inserting pre-defined
logic with a single line.

```
build_style = "meson"
```

Simply with this, you declare that this template uses the Meson build
system. What actually happens is that the build style will create some
of the necessary functions (`do_build` etc) implicitly.

A build style is a Python file in `cbuild/build_style` and looks like
this:

```
def do_configure(self):
    pass

def do_build(self):
    pass

def do_install(self):
    pass

def use(tmpl):
    tmpl.do_configure = do_configure
    tmpl.do_build = do_build
    tmpl.do_install = do_install

    tmpl.build_style_fields = [
        ("name", "default_value", str, False, False, False)
    ]
    tmpl.build_style_defaults = [
        ("make_cmd", "mything")
    ]
```

The template can further override pieces of the build style as necessary,
while the build style can set any functions it wants. It can also define
new template variables, as well as override default values for any
template variable.

In general, build styles are simply small wrappers over the `cbuild.util`
namespace APIs. That allows you to use the APIs when you need logic that
cannot be declared with just a simple variable, and keep templates simple
where that is sufficient.

There are currently a few build styles available.

##### cmake

You can generally use this for CMake-using projects.

Variables:

* `cmake_dir` A directory relative to `cwd` of the template that contains
  the root `CMakeLists.txt`. By default it is `None`, which means that it
  is directly in `cwd`.

Default values:

* `make_cmd` = `ninja`
* `make_build_target` = `all`

Sets `do_configure`, `do_build`, `do_check`, `do_install`.

Additionally creates `self.make`, which is an instance of `cbuild.util.make.Make`
for the template, with `build` `wrksrc`.

Implemented around `cbuild.util.cmake`.

##### configure

A simple style that simply runs `self.configure_script` within `self.chroot_cwd`
with `self.configure_args` for `do_configure` and uses a simple `Make` from
`cbuild.util` to build.

Sets `do_configure`, `do_build`, `do_check`, `do_install`.

You are expected to supply all other logic yourself. This build style works
best when you need a simple, unassuming wrapper for projects using custom
configure scripts. For `autotools` and `autotools`-compatible systems, use
`gnu_configure`.

Additionally creates `self.make`, which is an instance of `cbuild.util.make.Make`
for the template, with no other changes.

##### gnu_configure

A more comprehensive `build_style`, written around `cbuild.util.gnu_configure`.

Sets `do_configure`, `do_build`, `do_check`, `do_install`.

During `do_configure`, `gnu_configure.replace_guess` is called first, followed
by `gnu_configure.configure`.

Additionally creates `self.make`, which is an instance of `cbuild.util.make.Make`
for the template, with `build` `wrksrc`, and `env` retrieved using the
`gnu_configure.get_make_env` API.

All of this means that `gnu_configure` can implicitly deal with cross-compiling
and other things, while `configure` can't.

##### gnu_makefile

A simple wrapper around `cbuild.util.make`.

Variables:

* `make_use_env` A boolean (defaults to `False`) specifying whether some of the
  core variables will be provided solely via the environment. If unset, they
  are provided on the command line. These variables are `OBJCOPY`, `RANLIB`,
  `CXX`, `CPP`, `CC`, `LD`, `AR`, `AS`, `CFLAGS`, `FFLAGS`, `LDFLAGS`, `CXXFLAGS`
  and `OBJDUMP` (the last one only when not bootstrapping) during `do_build`.
  All of these inherently exist in the environment, so if this is `True`, they
  will simply not be passed on the command line arguments.

Sets `do_configure`, `do_build`, `do_check`, `do_install`.

The `install` target is always called with `STRIP=true` and `PREFIX=/usr`.

Additionally creates `self.make`, which is an instance of `cbuild.util.make.Make`
for the template, with no other changes.

##### meson

You can use this for Meson-using projects.

Variables:

* `meson_dir` A directory relative to `cwd` of the template that contains
  the root `meson.build`. By default it is `None`, which means that it
  is directly in `cwd`.

Default values:

* `make_cmd` = `ninja`
* `make_build_target` = `all`

Sets `do_configure`, `do_build`, `do_check`, `do_install`.

Additionally creates `self.make`, which is an instance of `cbuild.util.make.Make`
for the template, with `build` `wrksrc`.

Implemented around `cbuild.util.meson`.

##### python_module

A build style for Python modules (using `setup.py`).

Sets `do_build`, `do_check`, `do_install`.

The `do_build` executes `setup.py` with `python`, with the `build` target
plus any `self.make_build_args`.

The `do_install` executes `setup.py` with `python`, with the `install` target
and arguments `--prefix=/usr`, `--root={self.chroot_destdir}` plus any
`self.make_install_args`.

<a id="subpackages"></a>
#### Subpackages

The `cbuild` system has support for subpackages. Subpackages are just
regular packages repository-wise, except they are built as a part of
some main package's process, and are created from its files.

Subpackages are used for a variety of things, such as separating
development files from the main package, or for plugins.

There are two ways to register a subpackage in a template. These two
ways are mutually exclusive, with the `subpackages` array taking preference.
Therefore, when deciding, pick the one better suited for your template.

In either case, you should create a symbolic link named like the subpackage
in the respective repo category and have it point to the directory with the
main package template.

The simpler way to define a subpackage in the template is through a decorator.
This decorator is available globally during the time a package is initialized.
The syntax works like this:

```
@subpackage("mysubpackage")
def _subpkg(self):
    ...
```

The function name is up to you, it does not matter. In order to cover more
cases, the subpackage definition can also be conditional:

```
@subpackage("mysubpackage", foo == bar)
def ...
```

The subpackage will only be defined if the condition argument is `True`.

The more complicated way is through the `subpackages` template variable.
This is basically just an array of 2-tuples, where the first field in
the tuple is the subpackage name and the second field is the function
reference. The actual function body is identical for both approaches.

```
def _subpkg(self):
    ...

subpackages = [("mysubpackage", _subpkg)]
```

Usually the decorator way is better for most cases, while the array way
is better if your subpackage set varies a lot conditionally, or if you
want to ensure different ordering for subpackage population than listed
in the template.

The subpackage body function can then look like this:

```
def _devel(self):
    self.short_desc = short_desc + " - development files"
    self.depends = [...]
    self.options = ["textrels"]

    return ["usr/include", "usr/lib/*.so", "usr/lib/*.a"]
```

How this works should be fairly self-explanatory, but to make it clearer,
the function assigns template variables that apply to subpackages and
returns an array of files or directories to "steal" from the main
package. This is why subpackage ordering can be important; sometimes
some files may overlap and you may need to ensure some subpackages
"steal" their files first.

The `self` argument here is the subpackage handle.

If better control over the files is needed, you can also return a function
instead of a variable. The function takes no arguments (you are supposed
to nest this function and refer to the subpackage via its parent function)
and can use `self.take(...)` and the likes.

The following variables apply to subpackages. Most do not inherit their
value from the parent and are assigned the defaults; some are inherited,
those are explicitly marked.

* `short_desc` (inherits)
* `options`
* `depends`
* `provides`
* `skiprdeps`
* `nostrip_files`
* `hardening`
* `nopie_files`
* `shlib_provides`
* `shlib_requires`
* `triggers`

The `hardening` option does not actually do anything (since subpackages do
not affect the build) and its sole purpose is to be able to turn off the PIE
check for subpackages (as projects may build a mixture of PIE and non-PIE
files).

<a id="template_options"></a>
#### Template Options

There are various options you can specify as a part of the `options` variable.
Some of them can only be specified at the top level, while some also apply
to subpackages.

The following options are toplevel-only, i.e. they apply globally within
the template including for subpackages:

* `bootstrap` *(false)* This option specifies that the template is built
  during bootstrapping. Other templates will fail to build unless a build
  container is available.
* `textrels` *(false)* By default, if `cbuild` finds textrels within any
  ELF files in the packages, it will error. It is possible to override
  this by enabling the option.
* `parallel` *(true)* By disabling this, you can enforce single-threaded
  builds for the template. By default the number of build jobs passed
  by `cbuild` is respected.
* `debug` *(true)* By default, debug packages (`-dbg`) are generated if
  there are any strippable debug symbols. By setting this to `false`,
  you can disable passing of debug options to the compiler, as well as
  prevent generation of debug packages.
* `check` *(true)* By disabling this you can ensure the `check` phase
  is never run, even if enabled and enforced in the build system.
* `cross` *(true)* If disabled, the template will error early when
  attempting cross compilation.

The following options apply to a single package and need to be specified
for subpackages separately if needed:

* `scanrdeps` *(true)* This specifies whether automatic runtime dependencies
  are scanned for the package. By default, ELF files are scanned for their
  dependencies, which is usually desirable, but not always.
* `scanshlibs` *(true)* If disabled, the package will not be scanned for
  shared libraries to be provided by the package.
* `strip` *(true)* If disabled, ELF files in this package will not be
  stripped, which means debug symbols will remain where they are and
  debug package will not be generated.

<a id="hardening_options"></a>
#### Hardening Options

The `cbuild` system implements an automatic way to deal with toggling
different hardening options.

Currently the following options are always enabled by default:

* `fortify` Toggles `-D_FORTIFY_SOURCE=2`.
* `pie` Position-independent executables.
* `relro` Full RELRO.
* `ssp` Enables `-fstack-protector-strong`.

The following options are only enabled on targets where the toolchain
supports it (currently `ppc64le`, `ppc64` and `x86_64`):

* `scp` Enables `-fstack-clash-protection`.

<a id="tools"></a>
#### Tools

The build system also provides separate management of tools for convenience.
Tools in this case refer primarily to the toolchain.

By default, the following tools are defined:

* `CC` The C compiler, `clang` by default.
* `CXX` The C++ compiler, `clang++` by default.
* `CPP` The C preprocessor, `clang-cpp` by default.
* `LD` The linker, `ld.lld` by default.
* `PKG_CONFIG` The `pkg-config` implementation, `pkg-config` by default.
* `NM` The `nm` tool, `llvm-nm` when not bootstrapping, `nm` otherwise.
* `AR` The `ar` archiver, `llvm-ar` when not bootstrapping, `ar` otherwise.
* `AS` The assembler, `clang` by default.
* `RANLIB` The `ranlib` tool, `llvm-ranlib` when not bootstrapping
  and `ranlib` otherwise.
* `STRIP` The `strip` tool, `llvm-strip` when not bootstrapping
  and `strip` otherwise.
* `OBJDUMP` The `objdump` tool, `llvm-objdump`, and not provided
  when bootstrapping (ELF Toolchain does not provide it).
* `OBJCOPY` The `objcopy` tool, `llvm-objcopy` when not bootstrapping
  and `objcopy` otherwise.
* `READELF` The `readelf` tool, `llvm-readelf` when not bootstrapping
  and `readelf` otherwise.

When invoking commands within the sandbox, the build system will export
the values as environment variables, but before user provided environment
variables are exported (therefore, actual explicit env vars take priority).

The `CC`, `CXX`, `CPP`, `LD` and `PKG_CONFIG` tools are treated specially
for cross-compiling targets; when a cross-compiling target is detected,
the short tripet is prepended. This also happens when the user overrides
the tool via the `tools` variable in the template. Therefore, if you set
`CC` to `foo` and you cross-compile to `aarch64`, you may get something
like `aarch64-linux-musl-foo`.

Additionally, these tools are also exported into the environment with
their host values, as `BUILD_CC`, `BUILD_LD` and so on. This is to ensure
that project build systems can utilize both host and target toolchains
where appropriate.

There are many more variables that are implicitly exported into the
environment, but those are documented elsewhere.

<a id="build_profiles"></a>
### Build Profiles

The `cbuild` system allows for flexible definition of profiles for
different target architectures. These profiles are used for both
native and cross builds.

The definition exists in `cbuild/build_profiles/ARCH.ini` where `ARCH`
is the `apk` architecture name (in general matching `uname -m`).

It may look like this:

```
[profile]
cflags   = -march=rv64gc -mabi=lp64d
cxxflags = ${cflags}
fflags   = ${cflags}
endian   = little
wordsize = 64
triplet  = riscv64-unknown-linux-musl
```

These are also the fields it has to define. The `triplet` must always
be the full triplet (`cbuild` will take care of building the short
triplet from it if needed). The compiler flags are optional.

There is also the special `bootstrap` profile used when bootstrapping.
It differs from regular profiles in that the endianness and word size
are implied from the host, and the flags contain more things as the
user provided flags from `cbuild` are ignored when bootstrapping.

Unlike other profiles, `bootstrap` may also provide per-architecture
sections.

The `cbuild` system provides special API to manipulate profiles, and
you can utilize any arbitrary profiles within one build if needed.
More about that in the respective API sections, but the API allows
one to retrieve compiler flags in proper architecture-specific way,
check if we are cross-compiling and otherwise inspect the target.

<a id="build_environment"></a>
### Build Environment

This section of the documentation defines what the build environment
looks like when building a package.

Except when bootstrapping from scratch, most of the actual build process
runs sandboxed. The sandboxing is provided by the means of a minimal
Chimera container (as defined by the `main/base-chroot` package) and
the `bwrap` tool (`bubblewrap`), which utilizes Linux Namespaces to
provide a safe and unprivileged environment.

During initial setup, all required dependencies are installed. The
root is mounted read-write during this stage, and network access is
still available. This stage is considered trusted; no shell code is
executed.

When cross-compiling, the toolchain pieces required for the target
architecture are installed (e.g. `base-cross-aarch64` for `aarch64`).
The target dependencies are installed not in the container directly,
but rather in the target sysroot, which is `/usr/aarch64-linux-musl`
in the container (as an example for `aarch64`).

In order to trick `apk` into managing the sysroot properly, the system
automatically creates an internal dummy metapackage. This is needed so
that installing packages into the sysroot does not overwrite files
provided by the container's cross toolchain packages, this includes
things like `musl` as well as `libcxx`, `libunwind` and other bits
that are a part of the cross-toolchain and should not be installed
as regular packages (which they otherwise would, as dependencies).

Once the environment is set up and template code runs, the root is
always mounted as read only. That prevents unintended modifications
to the container, ensuring that it always remains consistent.

The following environment variables are exported into the sandbox:

* `PATH` The executable path, includes `/usr/bin` plus possible
  additions for `ccache` and so on.
* `SHELL` Set to `/bin/sh`.
* `HOME` Set to `/tmp`.
* `LC_COLLATE` Set to `C`.
* `LANG` Set to `en_US.UTF-8`.
* `SOURCE_DATE_EPOCH` The timestamp for reproducible builds.
* `CBUILD_STATEDIR` Points to where current package build metadata
  is stored, such as stamps for finished phases.
* `CFLAGS` Target C compiler flags.
* `FFLAGS` Target Fortran compiler flags.
* `CXXFLAGS` Target C++ compiler flags.
* `LDFLAGS` Target linker flags.
* `CC` Target C compiler.
* `CXX` Target C++ compiler.
* `CPP` Target C preprocessor.
* `LD` Target linker.
* `PKG_CONFIG` Target `pkg-config`.
* `CBUILD_TARGET_MACHINE` Target `apk` machine architecture.
* `CBUILD_TARGET_TRIPLET` Full target triplet (as described in profile).
  This is not exported during stage0 bootstrap.
* `BUILD_CFLAGS` Host C compiler flags.
* `BUILD_FFLAGS` Host Fortran compiler flags.
* `BUILD_CXXFLAGS` Host C++ compiler flags.
* `BUILD_LDFLAGS` Host linker flags.
* `BUILD_CC` Host C compiler.
* `BUILD_CXX` Host C++ compiler.
* `BUILD_CPP` Host C preprocessor.
* `BUILD_LD` Host linker.
* `BUILD_PKG_CONFIG` Host `pkg-config`.
* `CBUILD_HOST_MACHINE` Host `apk` machine architecture.
* `CBUILD_HOST_TRIPLET` Full host triplet (as described in profile).
  This is not exported during stage0 bootstrap.

Additionally, when using `ccache`, the following are also exported:

* `CCACHEPATH` The path to `ccache` toolchain symlinks.
* `CCACHE_DIR` The path to `ccache` data.
* `CCACHE_COMPILERCHECK` Set to `content`.
* `CCACHE_COMPRESS` Set to `1`.
* `CCACHE_BASEDIR` Set to the `cbuild`-set current working directory.

When set in host environment, the variables `NO_PROXY`, `FTP_PROXY`,
`HTTP_PROXY`, `HTTPS_PROXY`, `SOCKS_PROXY`, `FTP_RETRIES`, `HTTP_PROXY_AUTH`
are carried over into the environment.

The values of the `tools` meta variable are also exported. Additionally,
values of the `env` meta variable are exported, taking priority over any
other values. Finally, when invoking code in the sandbox, the user of the
API may specify additional custom environment variables, which further
override the rest.

The container is entered with a specific current working directory. During
the all parts of `fetch` and `extract` this is the `builddir`. From `patch`
onwards this is `wrksrc`, and from `configure` onwards this is `build_wrksrc`
inside `wrksrc`. This applies to all parts of each phase, including `init`,
`pre` and `post`.

The current working directory may be overridden locally via API, either for
the template or for the specific container invocation.

The following bind mounts are provided:

* `/` The root, read-only.
* `/ccache` The `ccache` data path (`CCACHE_DIR`), read-write.
* `/builddir` The directory in which `distfiles` are extracted and
  which is the base for the template `cwd` (`wrksrc` is inside).
  Read-only during subpackage population and later.
* `/destdir` The destination directory for installing; packages will
  install into `/destdir/pkgname-version`, or when cross compiling,
  into `/destdir/triplet/pkgname-version`. Read only before `install`,
  and read-write for the `install` phase.
* `/sources` Read-only, points to where all distfiles are stored.
* `/dev`, `/proc` and `/tmp` are fresh (not bound).

Once the `fetch` phase is done, all possible namespaces are unshared.
This includes the network namespace, so there is no more network
access within the sandbox at this point.

<a id="hooks"></a>
### Hooks and Invocation

The `cbuild` system is largely driven by hooks. A hook is a Python source
file present in `cbuild/hooks/<section>`. Hooks take care of things such
as distfile handling, environment setup, linting, cleanups, and even
package generation and repo registration.

The section consists of the `init_`, `pre_`, `do_` or `post_` prefix plus
the phase name (`fetch`, `extract`, `patch`, `configure`, `build`, `check`,
`install` and `pkg`).

Hooks are stamp-checked, except the `init_` hooks which are run always.
They are called together with the corresponding phase functions (if such
phase function exists) defined in the template. Every hook defined in the
section directory is invoked, in sorted order. They use a numerical prefix
to ensure proper sorting.

A hook looks like this:

```
def invoke(pkg):
    pass
```

It takes a package (sometimes this may be a subpackage) and does not return
a value, though it may error.

This is the entire call chain of a template build. The `init:` and `pre:`
invocations mean `init_` or `pre_` hooks plus template function if available.

For `post:`, the order is reversed, with the function called first and the
hooks called afterwards. For `do_fetch` and `do_extract`, either the hooks
or the function are called but not both; the function overrides the hooks.
This allows templates to define custom behavior if needed, but fall back
to the defaults that are useful for most.

When `step:` is written, it means `init_` hooks and function called always,
followed by `pre_` hooks and function, followed by `do_` function and hooks,
followed by `post_` function and hooks. All steps have their `do_` function
optional (i.e. template does not have to define it) except `install`, which
always has to have it defined in the template.

1) `init`
2) init: `fetch`
3) pre: `fetch`
4) `do_fetch` OR `do_fetch` hooks
5) post: `fetch`
6) init: `extract`
7) `do_extract` OR `do_extract` hooks
8) post: `extract`
9) step: `patch`
10) step: `configure`
11) step: `build`
12) step: `check`
13) step: `install`

The `install` step is also special in that it does not call `post_install`
hooks yet (`post_install` function is called though).

After this, subpackage installation is performed. For each subpackage, the
following is run:

1) subpackage is checked for `pkg_install`
2) if defined, `pre_install` hooks are called, followed by `pkg_install`
3) `post_install` hooks are called always

Finally, `post_install` hooks are called for the main package.

For both subpackages and main package, the system scans for shared libraries
in the package, before `post_install` hooks are called.

Once done, `init_pkg` hooks are called for the main package. Then, for each
subpackage, `pre_pkg` hooks are called, followed by the template `pre_pkg`
function (which is special in this way). The same is done for the main
package afterwards (`pre_pkg` hooks and function).

Finally, `do_pkg` and `post_pkg` hooks are called first for each subpackage
and then for the main package. After this, the build system rebuilds repo
indexes, removes automatic dependencies, and performs cleanup.

<a id="template_api"></a>
## Template API

The public API of `cbuild` that is accessible from templates consists of
exactly 2 parts: the API available as a part of the template handle, and
the API in the `cbuild.util` module namespace.

The template handle provides the important APIs that cannot be reimplemented
using other APIs. The utility namespace, on the other hand, provides things
that are useful to have implemented in a unified manner, but are implemented
in terms of the existing interfaces.

There are also several builtin global variables that are accessible from
the template scope at the time the template itself is executed. These are
only available during that time, and never after that, so do not attempt
to access them from inside functions.

<a id="api_builtins"></a>
### Builtins

#### @subpackage(name, cond = True)

This is a subpackage decorator, see [Subpackages](#subpackages).

#### current

Using `current`, you can access the `Template` handle from the global scope.
Keep in mind that at this point, it is uninitialized - not even things run
during the `init()` call are set up.

<a id="api_handle"></a>
### Handle API

The handle API consists of 3 classes. The `Package` class provides base API
that is available from both the main template and subpackage handles. The
`Template` class represents the template handle available as `self` in
global functions, while the `Subpackage` class represents the object in
subpackages.

Both `Template` and `Subpackage` inherit from `Package`.

<a id="class_package"></a>
#### Package Class

Shared API for both templates and subpackages.

All APIs may raise errors. The user is not supposed to handle the errors,
they will be handled appropriately by `cbuild`.

Filesystem APIs take strings or `pathlib` paths.

##### self.pkgname

A string representing the name of the package.

##### self.pkgver

A string representing the canonical versioned package name string. This
follows the `apk` format if `{pkgname}-{version}-r{revision}`.

##### self.version

The version number of the package. While provided as a template variable,
this is inherited into subpackages as well, so it's considered a part of
the base API.

##### self.revision

The revision number of the package. While provided as a template variable,
this is inherited into subpackages as well, so it's considered a part of
the base API.

##### self.logger

Represents an instance of a class with this API:

```
class Logger:
    def out_plain(self, msg, end = "\n")
    def out(self, msg, end = "\n")
    def warn(self, msg, end = "\n")
    def out_red(self, msg, end = "\n")
```

The `out_plain()` method writes out the given string plus the `end`.
The `out()` method does the same, but in a colored format and prefixed
with the `=> ` string.

The `warn()` method prints out `=> WARNING: <msg><end>` in a warning
color. The `out_red` is like `out`, except in red, providing a base for
printing out errors.

Whether the color-using methods use colors or not depends on the current
configuration of `cbuild` (arguments, environment, whether we are in an
interactive terminal are all things that may disable colors).

##### self.options

A dictionary representing the enabled/disabled options for the template
or subpackage. It is one of the few member variables that actually override
the template variables; within the template, you specify `options` as a
list, but that is not useful for checking, so the system internally maps
it to an array (and fills in the defaults as well, so you can check for
options the template did not explicitly set).

Usage:

```
if not self.options["strip"]:
    ... do something that only happens when stripping is disabled ...
```

##### self.destdir

The absolute path to the destination root of the template or subpackage.
This directory will be populated during the `install` phase and represents
the target root.

##### self.chroot_destdir

Same as `destdir`, but when viewed from inside the sandbox.

##### self.statedir

The absolute path to the directory (stored within `builddir`) which
contains all the state files (i.e. tracking which phases are done and
so on in a persistent manner to allow resuming, plus any wrappers).

##### def log(self, msg, end = "\n")

Using `self.logger.out()`, print out a specially prefixed message. The
message has the format `<name>: <msg><end>`, where `name` is either
`self.pkgver`, `self.pkgname` or fallback `cbuild`, in the order of
availability.

##### def log_red(self, msg, end = "\n")

Like `log`, but using `out_red`.

##### def log_warn(self, msg, end = "\n")

Like `log`, but using `warn`.

##### def error(self, msg, end = "\n")

In addition to logging a message like `log_red`, also raises an error,
which will abort the build.

##### def pushd(self, dirn)

To be used as a context manager. Temporarily changes the `cwd` as well
as `chroot_cwd` of the template to point to `dirn` (which is treated
as a relative path to current `cwd`).

This is pretty much an equivalent of the Unix `pushd`/`popd` commands.

Usage:

```
with self.pushd("src"):
    pass
```

##### def cp(self, srcp, destp, recursive = False, symlinks = True)

Copies `srcp` to `destp`. Both paths are considered potentially relative
to `cwd`. If `srcp` is a file, it is copied into `destp` if a directory,
or becomes `destp`. If `symlinks` is `True`, symlinks are followed, i.e.
if `srcp` was a symlink, the result will be a copy of the file it resolves
to.

If `srcp` is a directory, `recursive` must be `True` else the function
will error. This includes the case when `srcp` is a symbolic link to a
directory. In the latter case, `srcp` is copied as-is to `dest` like
if it was a file, and `symlinks` is ignored. The meaning of `symlinks`
is the opposite for directories with `recursive`, if it is `True`, all
symlinks are preserved, otherwise they are resolved.

This mimics the behavior of the Unix `cp` tool.

##### def mv(self, srcp, destp)

Moves `srcp` to `destp`. If `destp` is an existing directory, `srcp` is
moved into that directory, otherwise `srcp` is renamed to `destp`.
Both paths are considered potentially relative to `cwd`.

This mimics the behavior of the Unix `mv` tool.

##### def ln_s(self, srcp, destp, relative = False)

Creates a symlink at `destp` pointing to `srcp`. The `dest` is considered
potentially relative to `cwd`. If `destp` resolves to a directory, the
symlink is created inside that directory (including if it is a symlink
to a directory). In that case, the symlink's name will be the name
portion of `srcp`.

When `relative` is `True`, `srcp` is resolved to be relative to `destp`
using `os.path.relpath`; otherwise it is not modified in any way and
used as the target as-is. It can be a `pathlib` path or a string, just
like `destp`.

This mimics the behavior of the Unix `ln` tool with the `-s` switch and
optionally with `-r`.

##### def chmod(self, path, mode)

Changes the mode of `path` to `mode`. Usually you will want to use the
octal notation (e.g. `0o644` for owner-writable, all-readable). The
`path` is considered potentially relative to `cwd`.

This mimics the behavior of the Unix `chmod` tool.

##### def copy(self, src, dest, root = None)

Copies a file pointed to by `src` (relative to `cwd`) to `dest` (which must
be a relative path in `destdir`). If `dest` is a directory, the file will
be copied into it, otherwise it will be created there.

The `src` may be an aboslute path. If `root` is specified, it will be used
instead of `destdir`.

##### def unlink(self, f, root = None, missing_ok = False)

Removes `f`, which must refer to a file and must not be absolute. If
`missing_ok` is `True`, no error will be raised if non-existent.

If `root` is given, the `f` will be relative to it, otherwise `destdir`
is used.

##### def rmtree(self, path, root = None)

Removes the directory `path` (it must point to a directory, not a file).
The `path` must not be absolute, it will be considred relative to `root`,
unless not provided (in which case `destdir` is used).

##### def find(self, pattern, files = False, root = None)

Returns a generator object. For glob pattern `pattern`, search for files
within `root` (or `destdir`). Each result is a `pathlib.Path` object that
matches `pattern` and is relative (to `root`). The globbing is recursive.

Usage:

```
# finds every python script inside destdir, recursively
for p in self.find("*.py"):
    ...
```

<a id="class_template"></a>
#### Template Class

APIs not available on subpackages.

##### self.cross_build

A boolean specifying whether this is a cross build (to another architecture).

##### self.conf_jobs

The number of configured jobs to use for building. This is not affected
by whether parallel builds are disabled via options, always referring
to the number provided by `cbuild`.

##### self.make_jobs

The number of jobs to use for building. Unlike `conf_jobs`, this will always
be 1 if `parallel` option is disabled.

##### self.force_mode

Whether the build was forced (boolean).

##### self.bootstrapping

Whether we're currently bootstrapping stage 0 (i.e. no sandbox, no container).

##### self.run_check

Whether running the `check` phase is enabled by `cbuild`.

##### self.build_dbg

Whether building `dbg` packages is enabled by `cbuild`.

##### self.use_ccache

Whether using `ccache` is enabled by `cbuild`

##### self.build_profile

The current build profile handle. Represents a `Profile` object, which
has the following interface:

```
class Profile:
    arch = ...
    triplet = ...
    short_triplet = ...
    sysroot = ...
    hardening = ...
    wordsize = ...
    endian = ...
    cross = ...

    def get_cflags(self, extra_flags = [], debug = False, hardening = [], shell = False)
    def get_cxxflags(self, extra_flags = [], debug = False, hardening = [], shell = False)
    def get_fflags(self, extra_flags = [], debug = False, hardening = [], shell = False)
    def get_ldflags(self, extra_flags = [], hardening = [], shell = False)

    def has_hardening(self, hname, hardening = [])
```

The properties have the following meanings:

* `arch` The `apk` architecture name of the profile.
* `triplet` The "long" target triplet (e.g. `aarch64-unknown-linux-musl`)
* `short_triplet` The "short" target triplet (e.g. `aarch64-linux-musl`)
* `sysroot` A `pathlib` path representing the sysroot.
* `hardening` A list of hardening options for the profile.
* `wordsize` The integer word size of the target (typically 64 or 32).
* `endian` The endianness of the target (`little` or `big`).
* `cross` A boolean that is `True` for cross compiling targets and
  `False` otherwise.

There is a special `bootstrap` profile where the `triplet` and `short_triplet`
are `None`.

The `sysroot` refers to `/` for native targets and `/usr/<short_triplet>` for
cross-compiling targets.

The `get_cflags`, `get_cxxflags`, `get_fflags`, `get_ldflags` and `get_hardening`
correspond to the equivalently named methods on `Template`, except they are
not influenced by the template's configuration. The `Template` methods are
actually implemented on top of those (passing the template's information
using the arguments as necessary).

In general, you will not want to use the profile's methods, and the member
variables are strictly read only.

##### self.cwd

The current working directory of the template. This does not mirror the
actual current working directory of the OS; it is the directory that is
used strictly by the Python APIs of `cbuild`.

##### self.chroot_cwd

Like `cwd`, but when viewed from inside of the sandbox. In general you
will use this when building paths for commands to be executed within,
as using `cwd` directly would refer to a non-existent or incorrect
path.

##### self.template_path

The absolute path to the directory with `template.py`.

##### self.files_path

The absolute path to the `files` directory of the template. This directory
contains auxiliary files needed for the build, shipped in `cports`.

##### self.patches_path

The absolute path to the `patches` directory of the template. This directory
contains patches that are applied in the `patch` phase.

##### self.builddir

The absolute path to the `builddir`. This directory is where distfiles are
extracted, and which is used as the mutable base for builds.

##### self.chroot_builddir

Like `builddir`, but when viewed from inside the sandbox.

##### self.wrapperdir

A directory within `statedir` (an absolute path to it) that is used for
wrappers. This is added to `PATH` when executing commands within the sandbox,
in order to override or wrap certain tools where we don't want the default
behavior.

##### self.destdir_base

The base directory (absolute path) where all destination directories for
packages will be stored, i.e. for the main package as well as subpackages.

##### self.chroot_destdir_base

Like `destdir_base`, but when viewed from inside the sandbox.

##### def do(self, cmd, args, env = {}, wrksrc = None)

Execute a command in the build container, sandboxed. Does not spawn a shell,
instead directly runs `cmd`, passing it `args`. You can use `env` to provide
extra environment variables in addition to the implied ones (see the build
environment section). The provided env vars override whatever builtin ones
the system sets up.

The `wrksrc` is relative to current `cwd` of the template. If not given, the
working directory will be the current `cwd` of the template itself.

The level of sandboxing used depends on the current build phase. In all cases,
the root filesystem will be mounted read only, the `builddir` will be mutable
unless we're after `post_install`, the `destdir` will be immutable unless we
are at `install` phase, and all namespaces will be unshared (including network
namespace) unless we're at `fetch`.

Usage:

```
self.do("foo", ["--arg1", "--arg2"], wrksrc = "bar")
```

##### def stamp(self, name)

This is a utility API meant to be used as a context manager. It deals with
a stamp file (identified by `name`) in the current template `cwd`. You can
use it to have some code run just once, and once it succeeds, not have it
run again even if the same phase is run. You use it like this:

```
with self.stamp("test") as s:
    s.check() # this is important
    ... do whatever you want here ...
```

The `check()` method ensures that the code following it is not run if the
stamp file already exists. The script will proceed after the context.

##### def profile(self, target)

To be used as a context manager. Temporarily overrides the current build
profile to the given `target`, which can be a specific profile name (for
example `aarch64`) or the special aliases `host` and `target`, which refer
to the build machine and the target machine respectively (the target machine
is the same as build machine when not cross compiling).

Usage:

```
with self.profile("aarch64"):
    ... do something that we need for aarch64 at the time ...
```

##### def get_cflags(self, extra_flags = [], hardening = [], shell = False, target = None)

Get the `CFLAGS` to be used for a compiler. They will consist of the following:

1) Hardening `CFLAGS` as defined by current `hardening` of the template,
   possibly extended or overridden by the `hardening` argument.
2) The `CFLAGS` of the current build profile, possibly overridden by
   the `target` argument.
3) Bootstrapping or cross-compiling `CFLAGS`.
4) The `CFLAGS` of the template.
5) Any extra `CFLAGS` provided by `extra_cflags`.
6) Debug `CFLAGS` if set for the template.

The `target` argument is the same as for `profile()`.

The return value will be a list of strings, unless `shell` is `True`, in
which case the result will be a properly shell-escaped string.

##### def get_cxxflags(self, extra_flags = [], hardening = [], shell = False, target = None)

Identical to `get_cflags()`, but for C++.

##### def get_fflags(self, extra_flags = [], hardening = [], shell = False, target = None)

Identical to `get_cflags()`, but for Fortran.

##### def get_ldflags(self, extra_flags = [], hardening = [], shell = False, target = None)

Like `get_cflags()`, but to be passed when linking. Usually you will want
to pass the `CFLAGS` (or whatever your language is) followed by `LDFLAGS`.

##### def get_tool(self, name, target = None)

Get the specific tool (e.g. `CC`) for the current profile or for `target`.

The `target` argument is the same as for `profile()`.

This properly deals with cross-compiling, taking care of adding the right
prefix where needed and so on. It should always be used instead of querying
the `tools` member variable directly.

##### def has_hardening(self, hname, target = None)

Check if the current configuration (i.e. taking into account the template
as well as the current profile or the `target`) has the given hardening
flag enabled.

The `target` argument is the same as for `profile()`.

##### def install_files(self, path, dest, symlinks = True)

Installs `path` (which may be a file or a directory and is relative
to `cwd` of the template) to `dest` (which must refer to a directory,
and must not be absolute - it is treated as relative to `destdir`).

If `symlinks` is `True` (which is the default), symlinks in `path`
will also be symlinks in `dest`.

Usage:

```
self.install_files("data/foo", "usr/share")
```

##### def install_dir(self, *args)

For each argument, creates a directory in `destdir`. None of the arguments
must represent absolute paths.

Usage:

```
self.install_dir("usr/include", "usr/share")
```

##### def install_file(self, src, dest, mode = 0o644, name = None)

Installs `src` into `dest`, where `src` refers to a file (absolute or
relative to `cwd`) and `dest` refers to a directory (must exist and be
relative).

The destination file must not already exist. The permissions are adjusted
to `mode`, unless set to `None`. The destination file name will be `name`,
unless it is `None`, in which case the source file name is kept.

The `dest` is created if non-existent.

##### def install_bin(self, *args)

For each argument representing a file relative to `cwd`, install this file
in `usr/bin` and adjust the permissions. The file will be readable and
executable to all, and writable to owner only.

The path is created if non-existent.

##### def install_lib(self, *args)

For each argument representing a file relative to `cwd`, install this file
in `usr/lib` and adjust the permissions. The file will be readable and
executable to all, and writable to owner only. Meant to be used for dynamic
libraries, static library archives should use `install_file`.

The path is created if non-existent.

##### def install_man(self, *args)

For each argument representing a file relative to `cwd`, install this file
as a manpage. That means installing into `usr/share/man` into the right
section determined by the input file name. For example, if the file is
`foo.1`, it will be installed into `man1`. The permissions will be `644`.

If the input file does not have a section number or it is invalid, an error
is raised.

All paths are created as necessary.

##### def install_license(self, *args)

For each argument representing a path to a license file relative to `cwd`,
install this into `/usr/share/licenses/{pkgname}` with permissions `644`.

##### def install_link(self, src, dest)

Creates a symbolic link at `dest`, pointing to `src`.

Usage:

```
self.install_link("libfoo.so.1", "usr/lib/libfoo.so")
```

<a id="class_subpackage"></a>
#### Subpackage Class

These methods are only available on subpackage objects. You cannot create
a subpackage object directly, but it can be passed to hooks as well as
certain user defined functions.

##### def take(self, *args)

For each argument, the subpackage will "steal" the path from the main
package. The arguments can be strings or `pathlib` paths, representing
relative paths to `destdir` of the main package.

You will want to use this if you return a function from the subpackage
function. The following are equivalent:

```
def _subpkg(self):
    ...
    return ["usr/include", "usr/lib/*.a", "usr/lib/*.so"]

def _subpkg(self):
    ...
    def install():
        self.take("usr/include")
        self.take("usr/lib/*.a", "usr/lib/*.so")

    return install
```

<a id="api_util"></a>
### Utility API

Utility APIs exist in the `cbuild.util` namespace. They provide building
blocks for templates, built using the other available public API. You do
not have to actually use any of these building blocks from technical
standpoint, but you are highly encouraged to use them in practice, as
they simplify the template logic greatly.

#### cbuild.util.cmake

A wrapper for management of CMake projects.

##### def configure(pkg, cmake_dir = None, build_dir = "build", extra_args = [], cross_build = None)

Executes `cmake`. The directory for build files is `build_dir`, which
is relative to `chroot_cwd`. The root `CMakeLists.txt` exists within
`cmake_dir`, which is relative to `chroot_cwd` (when `None`, it is
assumed to be `.`).

The `pkg` is an instance of `Template`.

The `build_dir` is created if non-existent.

The arguments passed to `cmake` are in this order:

* `-DCMAKE_TOOLCHAIN_FILE=...`
* `-DCMAKE_INSTALL_PREFIX=/usr`,
* `-DCMAKE_BUILD_TYPE=None`,
* `-DCMAKE_INSTALL_LIBDIR=lib`,
* `-DCMAKE_INSTALL_SBINDIR=bin`,
* `pkg.configure_args`
* `extra_args`
* The directory for `cmake_dir`.

The `CMAKE_GENERATOR` environment variable is set to `Ninja` if `pkg.make_cmd`
is `ninja`, otherwise to `Unix Makefiles`.

An appropriate toolchain file is created when bootstrapping and when cross
compiling. You can prevent the creation of a toolchain file by explicitly
setting `cross_build` to `False`. That will ensure a native-like build even
when the profile is set to a cross-compiling one.

#### cbuild.util.compiler

A simple wrapper to directly invoke a compiler.

##### class GnuLike

A base class for a GNU-like compiler driver (such as Clang or GCC).

###### def __init__(self, tmpl, cexec, default_flags, default_ldflags)

The constructor. Sets the fields `template`, `cexec`, `flags` and `ldflags`.

The `cexec` argument is the compiler executable name (or path). The
flags arguments must be provided in the array form (not a string).

The `flags` are always passed for invocation, and `ldflags` only for linking.

###### def invoke(self, inputs, output, obj_file = False, flags = [], ldflags = [], quiet = False)

Invoke the compiler. Arguments will be passed in the following order:

* `self.flags`
* `inputs` Each entry is converted to `str`.
* `self.ldflags` if `obj_file` is `False`.
* `flags`
* `-c` if `obj_file` is `True`, `ldflags` otherwise.
* `-o`
* `output` (made absolute against `chroot_cwd`)

If `quiet` is `True`, the command will not be printed. Otherwise, the command
with all its arguments will be printed out via the logger before execution.

##### class C(GnuLike)

A C compiler. Like `GnuLike`, but more automatic.

###### def __init__(self, tmpl, cexec = None)

Calls `GnuLike.__init__`. If `cexec` is `None`, it defaults to `tmpl.get_tool("CC")`.
The `flags` are `tmpl.get_cflags()`, while `ldflags` are `tmpl.get_ldflags()`.

##### class CXX(GnuLike)

A C++ compiler. Like `GnuLike`, but more automatic.

###### def __init__(self, tmpl, cexec = None)

Calls `GnuLike.__init__`. If `cexec` is `None`, it defaults to `tmpl.get_tool("CXX")`.
The `flags` are `tmpl.get_cxxflags()`, while `ldflags` are `tmpl.get_ldflags()`.

#### cbuild.util.gnu_configure

A wrapper for handling of GNU Autotools and compatible projects.

##### def configure(pkg, configure_dir = None, configure_script = "configure", build_dir = "build", extra_args = [], env = {})

First, `build_dir` is created if non-existent (relative to `cwd`). Then,
the `configure_script` is called (which lives in `configure_dir`, which
lives in `chroot_cwd`).

The `pkg` is an instance of `Template`.

These arguments are passed first:

* `--prefix=/usr`
* `--sysconfdir=/etc`
* `--sbindir=/usr/bin`
* `--bindir=/usr/bin`
* `--mandir=/usr/share/man`
* `--infodir=/usr/share/info`
* `--localstatedir=/var`

If cross-compiling, these are followed by `--build=TRIPLET` and `--target=TRIPLET`
which are automatically guessed from the profiles. Additionally, these
are also passed for cross mode:

* `--with-sysroot={sysroot}`
* `--with-libtool-sysroot={sysroot}`

When cross compiling, autoconf caches are exported into the environment, which
are described by the files in `cbuild/misc/autoconf_cache`. The `common_linux`
is parsed first, then `musl-linux`, `endian-(big|little)`, and architecture
specific files.

Architecture-specific cache files are:

* For 32-bit ARM, `arm-common` and `arm-linux`.
* For AArch64, `aarch64-linux`.
* For `ppc64` and `ppc64le`, `powerpc-common`, `powerpc-linux`, `powerpc64-linux`.
* For `x86_64`, `x86_64-linux`.

When not cross-compiling, the `musl-linux` cache file is still read and
exported.

The result of `get_make_env()` is also exported into the environment, before
anything else.

The `pkg.configure_args` are passed after the implicit args, finally followed
by `extra_args`. Additionally, `env` is exported into the environment, after
the cache files (so the environment dictionary can override any caches).

##### def get_make_env()

The Make environment to use when building Autotools-based projects.

Currently contains the `lt_cv_sys_lib_dlsearch_path_spec`, which is
set to `/usr/lib64 /usr/lib32 /usr/lib /lib /usr/local/lib`.

##### def replace_guess(pkg)

Given a `Template`, finds files named `*config*.guess` and `*config*.sub`
recursively and replaces them with fresh copies from `cbuild/misc`.

This provides an automated fixup for when projects ship with outdated
`config.guess` and `config.sub` which frequently miss `musl` support
or new targets such as `riscv64`.

#### cbuild.util.make

A wrapper around Make and Make-style tools.

##### class Make

###### def __init__(self, tmpl, jobs = None, command = None, env = {}, wrksrc = None)

Initializes the Make. The arguments can provide default values for various
settings, which can further be overridden in sub-invocations.

The `command` is the default `make` command (which is not necessarily
the actual command used). The `wrksrc` is relative to `cwd`.

###### def get_command(self)

The the actual command used. If `command` was provided via constructor,
that is considered the base, otherwise `self.template.make_cmd` is.

If not bootstrapping, that is then returned as-is. When bootstrapping,
more logic is taken to accommodate standard Linux host environments:

* If the command is `gmake` and the `gmake` command is not available,
  we fall back to `make`.
* If the command is `make` and the `bmake` command is available, we
  use `bmake` instead.

The reason this is done is that we use `make` by default for most
projects, but `make` on Chimera is NetBSD `bmake`, while on most
Linux systems this is GNU `make`. Meanwhile, if a template specifies
`gmake` as the command, we want GNU `make` to be used (which is
called `gmake` in Chimera) but `gmake` may not exist on regular
Linux distributions (where it's called just `make`).

This makes it compatible with both Chimera and regular Linux systems
as the `bmake` alias exists in both and `gmake` is still used when
requested and exists.

###### def invoke(self, targets = [], args = [], jobs = None, env = {}, wrksrc = None)

Invoke the tool, whose name is retrieved with `get_command()`. The
arguments are passed like this:

* `-jJOBS` where `JOBS` is `jobs` or `self.jobs` or `self.template.make_jobs`.
* `targets`, which can be a list of strings or a string, if a list all are
  passed, if a string the string is passed.
* `args`

The environment for the invocation is the combination of `self.env` and
the passed `env`, further passed to `self.template.do()`. The `wrksrc` is
either the `wrksrc` argument or `self.wrksrc`.

You can use this method as a completely generic, unspecialized invocation.

###### def build(self, args = [], jobs = None, env = {}, wrksrc = None)

Calls `invoke`. The `targets` is `self.template.make_build_target`, the
`args` are `self.template.make_build_args` plus any extra `args`. The
other arguments are passed as is.

###### def install(self, args = [], jobs = None, env = {}, default_args = True, args_use_env = False, wrksrc = None)

Calls `invoke`. The `targets` is `self.template.make_install_target` and
`jobs`, `wrksrc` are passed as is.

If `default_args` is `True`, `DESTDIR` is passed implicitly (set to the
value of `self.chroot_destdir`. The method of passing it depends on the
value of `args_use_env`. If that is `True`, it is passed in the environment,
otherwise it is passed on the arguments (as the first argument).

Other arguments that are passed as `self.template.make_install_args` plus
any extra `args`.

The `env` is passed as is, except when `DESTDIR` is passed via environment,
then it is passed together with that (user passed environment always takes
preference).

#### cbuild.util.meson

A wrapper for management of Meson projects.

##### def configure(pkg, meson_dir = None, build_dir = "build", extra_args = [])

Executes `meson`. The `meson_dir` is where the root `meson.build` is located,
assumed to be `.` implicitly, relative to `chroot_cwd`. The `build_dir` is
the directory for build files, also relative to `chroot_cwd`.

The `pkg` is an instance of `Template`.

The `build_dir` is created if non-existent.

The arguments passed to `meson` are in this order:

* `--prefix=/usr`
* `--libdir=/usr/lib`
* `--libexecdir=/usr/libexec`
* `--bindir=/usr/bin`
* `--sbindir=/usr/bin`
* `--includedir=/usr/include`
* `--datadir=/usr/share`
* `--mandir=/usr/share/man`
* `--infodir=/usr/share/info`
* `--sysconfdir=/etc`
* `--localstatedir=/var`
* `--sharedstatedir=/var/lib`
* `--buildtype=plain`
* `--auto-features=auto`
* `--wrap-mode=nodownload`
* `-Ddefault_library=both`
* `-Db_ndebug=true`
* `-Db_staticpic=true`
* `--cross-file=...` if cross-compiling
* `extra_args`
* `meson_dir`
* `build_dir`

When cross compiling, an appropriate cross file is automatically generated.

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
