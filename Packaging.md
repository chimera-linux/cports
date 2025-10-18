# The Chimera Linux packaging manual

This manual is supposed to provide a comprehensive reference for Chimera Linux
packaging, i.e. a comprehensive reference for the packaging format.

In general, things not described in the manual are not a part of the API and
you should not rely on them or expect them to be stable.

*Table of Contents*

* [Introduction](#introduction)
* [Categories](#categories)
* [Targets](#targets)
* [Quality Requirements](#quality_requirements)
  * [Correct Style](#correct_style)
  * [Writing Correct Templates](#correct_templates)
    * [Handling /etc](#handling_etc)
    * [Hardening Templates](#template_hardening)
* [Build Phases](#phases)
* [Package Naming](#naming)
  * [Bootstrap Packages](#bootstrap_packages)
* [Filesystem Structure](#filesystem_structure)
* [Template Structure](#template_structure)
  * [Template Variables](#template_variables)
  * [Template Functions](#template_functions)
  * [Architecture Patterns](#arch_patterns)
  * [Build Styles](#build_styles)
  * [Subpackages](#subpackages)
  * [Automatic Dependencies](#automatic_deps)
  * [Template Options](#template_options)
  * [Hardening Options](#hardening_options)
  * [Tools and Tool Flags](#tools)
  * [Triggers](#triggers)
* [Build Profiles](#build_profiles)
* [Build Environment](#build_environment)
* [Hooks and Invocation](#hooks)
  * [Custom Targets](#custom_targets)
* [Staging](#staging)
* [Template API](#template_api)
  * [Builtins](#api_builtins)
  * [Handle API](#api_handle)
    * [Package Class](#class_package)
    * [Template Class](#class_template)
    * [Subpackage Class](#class_subpackage)
  * [Utility API](#api_util)
* [Update Check](#update_check)
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
pkgver = "0.99.0"
pkgrel = 0
build_style = "makefile"
pkgdesc = "Simple package"
license = "BSD-3-Clause"
url = "https://foo.software"
source = f"https://download.foo.software/foo-{pkgver}.tar.gz"
sha256 = "ad031c86b23ed776697f77f1a3348cd7129835965d4ee9966bc50e65c97703e8"
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
$ ./cbuild pkg main/foo
```

The result will be a local repository containing the binary packages.

<a id="categories"></a>
## Categories

The Chimera packaging collection provides two categories in which templates
can go. These currently are:

* `main`
* `user`

Each category has its own repository that is named the same as the category.

The `main` category contains packaging that is maintained and/or approved
by committers and considered high quality. Most packaging in the distro
goes here.

The `user` category is a multi-purpose place; user-submitted templates go
here, as well as things of limited usefulness, things with incomplete
packaging, and `restricted` templates (typically things that are not
redistributable and do not have binary packages built). In some cases,
templates from here may be moved to `main` later.

If you are a new contributor, your templates should usually go in `user`.
An exception for this is when the template is a dependency of something in
a stricter category, or when a committer determines that it should go in
a stricter category (particularly for software that is useful to many people
and likely to be well tested). Trusted contributors active in the community
for a longer time may submit theirs in `main`. Random leaf packages that
contain shell scripts, themes, fonts, and so on should usually go in `user`.

Note that it is not supported to create your own categories. While the
mechanism they are implemented with is transparent and obvious and there
isn't anything that blocks you from doing so, it is purely an implementation
detail and subject to change in the future, especially with the template
resolution system still being WIP.

<a id="targets"></a>
## Targets

Chimera comes with multiple target architectures, and they may be divided
into roughly three categories:

1) Well supported architectures with repos
2) Worse supported architectures with repos
3) Architectures without repos

In the first case, there are complete official repositories backed by
reasonable build infrastructure, and we take care to run unit tests and
so on by default on such architectures.

In the second case, we still provide repos, but unit tests may or may
not be run or their failure may not be considered an error, not all
packages may be available, and their testing may not be on the same
level.

In the third case, the architecture has a certain level of support in
the packaging (i.e. there is a build profile, various templates and
build styles account for it, etc.) but there are no repos and no
official support.

Current architectures with best support:

* `aarch64` (generic)
* `ppc64le` (POWER8+)
* `x86_64` (generic)

Other architectures with repositories:

* `loongarch64` (generic, no LTO + unit tests enforced)
* `ppc64` (ppc970+, unit tests only run for reference)
* `ppc` (PowerPC 603+, unit tests only run for reference)
* `riscv64` (rv64gc, no LTO + unit tests not run)

Other possible targets:

* `armhf` (ARMv6 + VFP)
* `armv7` (ARMv7 + VFP)

<a id="quality_requirements"></a>
## Quality Requirements

In order to be included in `user`, there are few requirements. The software has
to provide something of usefulness to the users, must not be malicious, and
must not violate the project community guidelines. At the time of introduction,
it must satisfy the general style requirements and must be buildable, it will
receive a review from a maintainer and will be merged at their convenience.

For inclusion in `main`, it must be redistributable and must be open source,
when possible, it must be packaged from source code (except for e.g. bootstrap
toolchains), must be well maintained, and backed by an existing committer.
In general, it should not be a VCS version, i.e. it should refer to some kind
of stable tag, with some very rare exceptions. Vendoring of dependencies should
be avoided if viable. Drive-by contributions will not be accepted in `main`
directly in most cases. It must not be vetoed by anybody from core team.

<a id="correct_style"></a>
### Correct Style

The `cbuild` system as well as the templates are formatted with the
[Black](https://black.readthedocs.io/en/stable/) Python style. When writing
either template or `cbuild` code, make sure to run it through an automated
formatter too. Both `black` and `ruff format` are supported.

They should also pass [ruff check](https://astral.sh/ruff) and
[flake8](https://flake8.pycqa.org/en/latest) with our configuration, though
running the former is preferred, as ruff contains more checks than flake8 and is
what gets ran in CI.

<a id="correct_templates"></a>
### Writing Correct Templates

Most importantly, keep it simple. The `cbuild` system is designed to make
correct things easy and terse, and bad things ugly and complicated. If there
is any doubt (i.e. something you consider good but it is inconvenient to
write in `cbuild` templates) feel free to report it in the issue tracker.

Keep conditional stuff to a minimum. This includes:

1) Cross-compiling handling should be generalized to be the same for native
   in most cases. The system provides facilities to simplify doing that; for
   example handling of `sysroot` in profiles should be entirely transparent.
2) Cross-compiled packages should be functionally equal to native ones and
   have comparable contents. If this is not the case, the template is not
   eligible for cross-compilation.
3) There is no such thing as a native architecture and a cross architecture.
   Any architecture can be both (i.e. cross-compiling from ARM to x86_64 is
   actually a perfectly valid case and should be handled identically to
   doing it the other way around).
4) Templates should not perform any contents patching by themselves (e.g. like
   via `sed`) and especially not conditionally. A generic patch should be
   written instead.

You should never make any assumptions about the build environment. Things like
substituting specific default `CFLAGS` for something else is always wrong.
Instead, assume that the original value can be any, and if you need a specific
value, override it by passing it after the default.

Build styles should be used when appropriate. When not using build styles,
standard template variables should still be used, and expanded where necessary.

Build phases should be considered atomic, and builds should be considered
resumable. Do not store any in-memory state between build phases, as you
cannot be sure that the build will not be resumed from after the phase
has run. Use the `init_` template functions to deal with such state, as
they are guaranteed to run every time.

Care should be taken to avoid build-time dependency cycles. Cases where
building a package requires another package to be already built are always
wrong. Every package should be buildable with just a `bldroot` and an
entirely empty repository (i.e. `cbuild` should be able to build the
entire dependency tree at will). Sometimes this requires disabling tests
in the template (via `!check`). It is a good idea that even test suites
that cannot be run or are somehow broken and disabled by default are still
set up. That ensures someone can either find a solution later, fix it, or
at least be able to see which parts of the suite run successfully by forcing
the test run (as `cbuild` has an option to bypass `!check`).

The build environment takes care to minimize differences between possible
hosts the builds may be run in. However, there may always be edge cases,
and tests should not rely on edge cases - they must be reproducible across
all environments `cbuild` may be run in.

Also, Chimera systems should be stateless at their baseline. That means a
system can be recreated from its world file, and all mutable configuration
files are considered ephemeral. In practice this means:

1) Anything installed in `/usr` is considered immutable; the package manager
   should own all files and directories in there. This is generally already
   the case. If a directory needs to be empty and present in there, you should
   use the `file_modes` metadata to create them as `cbuild` will otherwise
   clean them.
2) Anything in `/etc` and `/var` is mutable and if the software in question
   allows, should not be owned by the package manager. Any directories and
   other state should be created through the `tmpfiles.d` mechanism, except
   when this does not make sense (e.g. the parent dir is already populated
   by the package and the new dirs are supplementary and so on). Notably, the
   `/var` directory is forbidden in packages. This results in a system where
   deletion of these dirs/files will result in them being re-created from
   scratch upon next boot.

<a id="handling_etc"></a>
#### Handling /etc

Frequently, properly dealing with `/etc` paths in packages can become
non-trivial. Currently there is a lot of templates that do not follow
the expected style, typically due to little support from the upstream
software.

The expectation in Chimera packages is that software does not install
default configuration files in `/etc`, this being the user's responsibility.
If possible however, software should still work by default.

There are multiple types of configuration handling that can affect the
way things can be packaged:

1) Software does not expect a configuration file to be in place by default,
   having builtin default settings. The user can create a configuration file
   in `/etc/somewhere` to alter the settings. Optionally, if upstream provides
   one, the package may install a sample in `/usr/share/etc/somewhere`.
2) Software expects a configuration file, but will not work or is not expected
   to work when used with a sample and requires user-supplied settings.
   In this case, it can be handled the same as case 1.
3) Software expects a configuration file in `/etc` and will not work without
   one, but a default sample is typically good enough to run a service, and
   does not expect it to be altered. In this case, the default configuration
   should be installed in `/usr/share/etc/somewhere` and the software should
   be made to use it preferentially when the `/etc` one does not exist already.
   For instance, if the software takes a command line argument or an environment
   variable to provide a config file path, a small wrapper script can be written
   for the purpose of a `dinit` service that checks for existence of the user
   file in `/etc` and if it does not exist, passes the argument or so on to
   make it use the systemwide default.
4) A case like the above, but with no way to externally handle this. In this
   case, patching the software downstream and/or convincing upstream to fix
   this properly should be considered. This is the worst case scenario. If
   everything else fails, it can be treated like case 2, and require user
   intervention before using it (with `/usr/share/etc` having a canonical
   tree).
5) Software that already does the right thing. A particular desired pattern
   is with `.d` directories that preferentially scan `/etc/foo.d` and then
   `/usr/lib/foo.d` or similar. Nothing to do here except making sure that
   packaging installs in the correct `/usr` paths.

There are some things not to do:

1) Install in random `/usr` paths. Things that require a systemwide config
   to be installed should mirror a proper `/etc` tree in `/usr/share/etc`,
   unless they already have their own builtin path that is expected by upstream.
2) Use `tmpfiles.d` to alter paths in `/usr`. This path is immutable, and should
   contain only world-readable, root-owned files.
3) Use `tmpfiles.d` to copy to `/etc` using the `C` command. This may seem like
   a good idea for the purpose of populating the path but has the major drawback
   of not tracking packaging changes; once copied once, it will not get updated,
   even if the package updates its files and the user has not altered the copy
   at all.

<a id="template_hardening"></a>
#### Hardening Templates

When writing new templates, care should be taken to use proper hardening
tags. While most hardening options that one should use are implicitly set
by default and there is no need to worry about them, there are hardening
options that cannot be default but should be set if possible anyway.

Hardening tags are specified using the `hardening` list metadata. Just like
the `options` list metadata, they can be enabled (e.g. like `foo`) or
disabled (e.g. like `!foo`).

##### Control Flow Integrity (CFI)

The Clang CFI is a particularly notable one. It cannot be enabled by default
as it breaks on a lot of packages, but those which it does not break with
can benefit from it. Packages that are broken with it can also be patched
(and patches upstreamed) in the ideal case.

CFI actually consists of multiple components, which can normally be used
individually when passing options to Clang, but cbuild groups them together.

CFI requires everything to be compiled with hidden visibility as well as
with LTO. Many libraries cannot be compiled with hidden visibility, as they
rely on default visibility of symbols. Programs can usually be compiled with
hidden visibility as by default they do not export any symbols. This is not
always the case, however, and it must be checked on case-by-case basis.

If you cannot enable hidden visibility nor LTO, then you cannot enable CFI.
Otherwise, toggle `vis` as well as `cfi` and test your template. If this
does not result in a regression (i.e. the package works, its tests pass
and so on), then it can be enabled on the tree.

The most often breaking component of CFI is the indirect function call
checker. Clang CFI is type-based, and therefore strict about types being
matched. That means the following will break, for example:

```
typedef void (*cb_t)(void *arg);

void foo(void *ptr, cb_t arg) {
    arg(ptr);
}

void cb(int *arg) {
    ...
}

void bar(void *x) {
    foo(x, (cb_t)&cb);
}
```

The reason this breaks is that we are calling `cb` through a different
function signature than `cb` is declared with.

Correct, CFI-compliant code in this case would be:

```
typedef void (*cb_t)(void *arg);

void foo(void *ptr, cb_t arg) {
    arg(ptr);
}

void cb(void *argp) {
    int *varg = argp;
    ...
}

void bar(void *x) {
    foo(x, &cb);
}
```

Other types of CFI usually do not break as much as they are either specific
to C++ (which is more strictly typed, especially in those contexts) or
overall less prone to such shortcuts.

Note that there are two other caveats to Clang CFI in our case:

1) It is not cross-DSO; checks are performed only within the executable
   or library and not for any external API. Correct cross-DSO CFI requires
   support in the C standard library.
2) It is currently only available on the `x86_64` and `aarch64` targets.
   On other targets it is silently ignored (so you do not need to set
   it conditionally).

##### Integer subset of UBSan

This one is notable as it has potential to break existing C/C++ code while
also being the default. The hardening string is `int`. All the cases it
traps are undefined behavior in C/C++, but codebases still commonly
violate those.

It enables the following:

* `signed-integer-overflow` Traps signed integer overflows.
* `integer-divide-by-zero` Traps integer division by zero.

Unsigned overflows are allowed as they are not undefined behavior.

An example of signed overflow:

```
int x = INT_MAX;
x += 1000;
```

The typical visible outcome of this is wrap-around, given the way two's
complement works. The compiler is allowed to do whatever it wants though,
and it is allowed to optimize assuming that this will never happen, given
it is undefined behavior.

Unsigned integers also wrap around, starting from 0 again.

Regardless of compiler optimization, integer overflows frequently result
in security vulnerabilities, which is why we harden this. In cases where
there are too many instances of the bug and it is not possible to patch
around it, it may be disabled with `!int` and a comment explaining why
this is done.

UBSan is available on all targets Chimera currently supports.

##### Identifying hardening traps

Sometimes it is possible to reproduce a crash with a production package in
Chimera. If you can recompile your program with sanitizer instrumentation,
it's usually very easy to tell what's going on. The `cbuild` system provides
an easy way to recompile a template with instrumentation on:

```
options = ["sanruntime"]
```

The sanitizer checks in packaged binaries are compiled in trapping mode, i.e.
without a runtime. That means when you run into a bug, you will get a vague
crash. On supported architectures, this will typically be a `SIGILL` in the
better case, but maybe `SIGABRT` elsewhere, where specific code has not been
implemented. With instrumentation on, you will instead get a more helpful
error message with a source file, line number, and reason.

However, sometimes instrumentation may not be possible, very often for libraries
and projects with strange/complicated build systems. In these cases identifying
the issue becomes more difficult. You will need debug symbols for the package
(usually you can install the `-dbg` package, don't forget about `musl-dbg` too)
and a debugger (`lldb`). Then you can run your program in the debugger, or
you can capture a core dump and open it in the debugger.

On architectures where `SIGILL` is emitted, it is usually possible to tell what
kind of sanitizer violation has happened. The instruction on which the program
aborts encodes this information. You need to get the current assembly
instruction in the debugger, and you might see something like this (example
on the `x86_64` architecture):

```
(lldb) x/1i $pc
->  0x5555555b0dc6 <+297814>: ud1l   0xc(%eax), %eax
```

Note the `ud1l` instruction, specifically the `0xc(%eax)`. The `0xc` encodes
the identifier of the sanitizer check. The full list is available here:

https://github.com/llvm/llvm-project/blob/main/clang/lib/CodeGen/CodeGenFunction.h#L112

At the time of writing, these were:

0. AddOverflow
1. BuiltinUnreachable
2. CFICheckFail
3. DivremOverflow
4. DynamicTypeCacheMiss
5. FloatCastOverflow
6. FunctionTypeMismatch
7. ImplicitConversion
8. InvalidBuiltin
9. InvalidObjCCast
10. LoadInvalidValue
11. MissingReturn
12. MulOverflow
13. NegateOverflow
14. NullabilityArg
15. NullabilityReturn
16. NonnullArg
17. NonnullReturn
18. OutOfBounds
19. PointerOverflow
20. ShiftOutOfBounds
21. SubOverflow
22. TypeMismatch
23. AlignmentAssumption
24. VLABoundNotPositive

In our case, `0xc` is the value 12. Counting in the list, starting with zero,
you can see this one is `MulOverflow`, which is a signed integer overflow
caused in multiplication expression. The backtrace will likely not have a
line number for the specific crash, as it's compiler-generated code. You can
however inspect the backtrace as well as disassembly and match it against the
context of the source code of the project in question, and often the reason
will be clear.

<a id="phases"></a>
## Build Phases

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

All build phases are run in either `self.srcdir` (all phases), or in
`build_wrksrc` inside that directory (`configure` and later); the `self.srcdir`
is created automatically.

* `setup` The build system prepares the environment. This means creating
  the necessary files and directories for the sandbox and installing the
  build dependencies. When cross-compiling, the cross target environment
  is prepared and target dependencies are installed in it. When the template
  defines a `fetch` function, this is run first, as the function may
  depend on the sandbox being set up. Otherwise, it is run second. The `deps`
  sub-phase can be invoked separately if needed.

* `fetch` During `fetch`, required files are downloaded as defined by the
  `source` template variable by default (or the `fetch` function of
  the template in rare cases). The builtin download behavior runs outside
  of the sandbox as pure Python code, which is typically run before `setup`.
  When overridden with `fetch`, it also overlaps with the `extract` stage
  as the function is supposed to prepare the `builddir` like `extract` would,
  and runs after `setup`.

* `extract` All defined sources (which are not marked as skipped) are extracted.
  The builtin behavior runs inside of the sandbox, except when bootstrapping.
  It populates the `self.srcdir`. The `self.srcdir` is not implied by sources.
  Instead, it is created automatically, and all sources are extracted in it.
  When the extraction would result in a single directory being present inside
  `self.srcdir`, which is often the case (as the common scenario is having a
  single source tarball and most tarballs don't have their files directly in
  the root), the contents of the directory are moved into `self.srcdir` and
  the leftover empty directory is removed. When `source_paths` is used and
  a source has a path that is not an empty string or `.`, it is extracted
  separately and is only moved into place after the moving logic is applied,
  while having the moving logic applied to itself as well. This simplifies
  various scenarios; for instance, one can have one tarball extract as if there
  was only one source (i.e. its contents become `self.srcdir`, including moving
  the contents if it contains a single directory) while having another tarball's
  contents become a subdirectory in the primary extracted tree, regardless of
  whether the secondary tarball has its files directly in root or whether it
  contains a directory.

* `prepare` The source tree is prepared for use. This does not do anything
  by default for most templates. Its primary use is e.g. with the `cargo`
  build system for Rust in order to vendor dependencies so they are ready
  for use by the time patches are applied (and thus they can be patched
  with the other stuff).

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
  after the template-defined `install` finishes. At the time the
  subpackages are populated, `builddir` is read-only in the sandbox.
  Ideally it would also be read-only during `install`, but that is
  not actually possible to ensure (since build systems like to touch
  their metadata and so on).

* `pkg` Create binary packages and register them into your local repo.
  During this point, `destdir` is also read-only for the sandbox.

* `clean` Clean up the `builddir` and `destdir`.

When building packages with `cbuild`, you can invoke only the specific
phase (from `fetch` to `pkg`). All phases leading up to the specified
phase are run first, unless already ran.

<a id="naming"></a>
## Package Naming

All packages should only use lowercase characters that are in the ASCII,
never mixed case, regardless of what the software is called.

In general, the primary package of the template (i.e. not a subpackage)
should follow the upstream name (other than case) regardless of the
contents of the package. That is, when a library is called `foo`,
the package should be called `foo`, not `libfoo`.

If you need to split one or more libraries from the main package,
the package should take on the `-libs` suffix. This should be the
default approach. However, if the library or libraries are a subproject
of the main project and are called `libfoo` upstream, you can use that
name. Additionally, the `lib` prefix can also be used in cases when
the main package is splitting off multiple libraries each into its
own subpackage (this should be done sparingly and mostly only when
combining the libraries would pull in unnecessary bulk, for example
through different dependencies).

Development packages should use the `-devel` suffix, like `foo-devel`
for the `foo` template. The convention with library subpackages and
devel packages is that if you have `foo` and `libfoo`, the development
files go in `foo-devel`. However, if the library part has its own
development files that make sense separately from the main `devel`
package, it is perfectly acceptable to have `libfoo-devel` alongside
`foo-devel`. If the template calls for having multiple `-devel`
packages related to different individual libraries, you can also
split them up accordingly.

Static libraries should go in `-static` packages in nearly all cases.
In specific cases, they will go in `-devel`. Static libraries are
automatically split from `-devel` (unless overridden with `!autosplit`
or `!splitstatic`) and are by default forbidden from other packages
than `-devel` or `-static` ones, so you should not have to declare
them manually.

In general, things packaging libraries should always have a `devel`
package of some sort, except in specific rare cases where this does
not make sense (e.g. development toolchains, where the primary package
is already a development package by itself; it may still be a good thing
to separate the runtime libraries in those cases).

Development packages should contain `.so` symlinks (where not required
at runtime) as well as include files, `pkg-config` files and any other
files required for development but not required at runtime.

Debug packages have the `-dbg` suffix and are created automatically in
most cases.

Various other packages are also created automatically. See the section
about automatic subpackages for more details.

If a primary package (typically a library or some kind of module) has
auxiliary programs that are separated into a subpackage, the subpackage
should be called `foo-progs`.

Subpackages for language bindings should put the language name in the
suffix, e.g. `foo-python`. However, language modules that are the primary
package should put that in the prefix, e.g. `python-foo`.

As far as general guidelines on subpackages go, things should be separated
as little as possible while still ensuring that people do not get useless
bloat installed. That means separating runtime libraries where they can
work on their own, always separating development packages, always separating
language bindings (where they bring a dependency that would otherwise not
be necessary) and so on.

<a id="filesystem_structure"></a>
## Filesystem Structure

Programs meant to be executed directly by the user always go in `/usr/bin`.
The `/usr/sbin`, `/bin` and `/sbin` paths are symbolic links to the
primary `/usr/bin` path and should never be present in packages.

Libraries go in `/usr/lib`. Do not use `/usr/lib64` or `/usr/lib32`,
these should never be present in packages. The same goes for the toplevel
`/lib` or `/lib64` or `/lib32` paths. In general, compatibility symlinks
are present in the system and they all point to `/usr/lib`.

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

<a id="bootstrap_packages"></a>
### Bootstrap Packages

Packages with the suffix `-bootstrap` are special, provided they are not
metapackages (`build_style = meta`). They will not be installable by default
in a regular system and represent either bootstrap builds of various software
needed to break dependency cycles in `cbuild` or bootstrap toolchains for
various programming language compilers.

Every package `foo-bootstrap` gains an implicit dependency on `bootstrap:cbuild`.

You can set up a virtual `bootstrap:cbuild` in your own environment:

```
$ apk add --virtual bootstrap:cbuild
```

<a id="template_structure"></a>
## Template Structure

A template consists of **variables** and **functions**. A simple template
may only consist of variables, while those that need to define some
custom behavior may also contain functions.

The template follows the standard Python syntax. Variables are assigned
like `foo = value`. Functions are defined like `def function(): ...`.

All template-global variables and functions that do not start with an
underscore must be recognized by `cbuild`, i.e. variables must be one
of the below, and functions must be one of the known hooks that are
permitted in templates. If you need to create e.g. custom helper functions
that are specific to the template or variables that are used in expansion
of other variables, begin them with a single underscore. This makes the
linter skip them.

<a id="template_variables"></a>
### Template Variables

In general, changes made to toplevel variables from inside functions are
not respected as variables are read and stored before the functions are
executed. Any later accesses to variables must be done through the template
handle passed to functions as the first argument (typically called `self`).

These variables are mandatory:

* `license` *(str)* The license of the project in SPDX license expression
  format (e.g. `BSD-3-Clause OR GPL-2.0-or-later`). The license should be
  a single expression. You can disable validation of the license by using
  the `!spdx` option (e.g. for custom licenses not covered by SPDX). The
  syntax supports custom license IDs via `custom:somename`. While this is
  not a part of the SPDX license expression specification, it can be used
  to cover e.g. dual license software with a custom and standard license
  via something like `custom:foo OR BSD-3-Clause`. Metapackages should
  always use license `custom:meta`. Public domain packages should always
  use `custom:none`. Packages that have some custom license should use
  `custom:packagename`, and properly install the license. The license
  is inherited into all subpackages, and subpackages are allowed to set
  it themselves. License exceptions can be from the standard list or they
  can be custom as well, e.g. `GPL-2.0-or-later WITH custom:foo-exception`.
* `pkgname` *(str)* The primary package name, must match template name.
  It must be lowercase, likewise for subpackages.
* `pkgver` *(str)* The package version, applies to all subpackages. Must
  follow the correct format for the `apk` package manager.
* `pkgrel` *(int)* The release number for the package. When changes are
  made to the template that require rebuilding of the package, this is
  is incremented by one. The initial value should be zero. When bumping
  to a new version, it should be reset back to zero.
* `pkgdesc` *(str)* A short, one line description of the package. Should
  be kept at 72 characters or shorter. In general, this should not begin
  with an article, and should not end with a period, and should not contain
  any subdescription ` (foo)` as that should be done with `subdesc`. The
  description is inherited into any subpackages, while `subdesc` may be
  filled in separately. It should use American English. See the section
  about subpackages for more details.
* `url` *(str)* The homepage URL of the project being packaged. To pass
  lint, the URL must have either the `http` or `https` scheme, must parse
  correctly and not have a trailing slash in the path.

There is also a variety of variables that are builtin but not mandatory.
Keep in mind that default values may be overridden by build styles.

* `archs` *(list)* A list of architecture patterns to determine if the template
   can be built for the current architecture. See "Architecture Patterns" below.
* `broken` *(str)* If specified, the package will refuse to build. The value
  is a string that contains the reason why the package does not build.
* `broken_symlinks` *(list)* A list of (possibly globbed) relative patterns
   matching what is allowed to be a broken symlink. This is preferrable to
   setting the brokenlinks option.
* `build_style` *(str)* The build style used for the template. See the
  section about build styles for more details.
* `build_wrksrc` *(str)* A subpath within `self.srcdir` that is assumed to be
  the current working directory during `configure` and later.
* `checkdepends` *(list)* This is like `hostmakedepends`, but only installed
  if the `check` option is enabled for the template and not cross-building.
  Note that these are installed even if the user explicitly chooses not to
  run tests, in order to ensure a reproducible build environment. It mostly
  exists to visually separate dependencies only needed for tests from
  the others.
* `compression` *(str)* Specifies the package compression. The default is
  unspecified (which means the global default will be used). Currently this
  can be `zstd`, `deflate`, and `none`, optionally with a compression level
  for the former two like `zstd:3` or `deflate:9`. You can also specify
  special values `slow` and `fast` which will respect the global compression
  but use special levels, as well as `zstd:fast`, `zstd:slow` and so on.
* `configure_args` *(list)* This list is generally specific to the build
  system the template uses. Generally speaking, it provides the arguments
  passed to some kind of `configure` script.
* `configure_env` *(dict)* Environment variables to be exported when running
  the configure script. The way passing them is implemented depends on the
  build system, but in general any user-provided environment at call site
  overrides this, while this overrides the global environment (`env`).
* `configure_gen` *(list)* The command used to generate the configure
  script. Used only by specific build styles.
* `configure_script` *(str)* The name of the script relative to current
  working directory used for configuration. Only used by build styles that
  use such scripts. The default value is `configure`.
* `debug_level` *(int)* The level to use when generating debug information
  in the compiler (i.e. `-gN` for C). By default, this is -1, which will
  determine it according to build profile (typically 2 for 64-bit targets,
  to match the default level of the compiler with `-g`, and 1 for 32-bit
  ones to avoid running out of memory).
* `depends` *(list)* Runtime dependencies of the package. They are not
  installed in the build container, but are checked for availability (and
  built if missing). While these may be just names, you can also specify
  constraints (e.g. `foo<=1.0-r1`) and conflicts (`!foo`). You can also
  specify dependencies on `pkgconf` files (`pc:foo`), executable commands
  (`cmd:foo`) and shared libraries (`so:libfoo.so.1`, though this is not
  recommended), as well as virtual packages (`virtual:foo`). Any virtual
  dependencies must explicitly specify a non-virtual provider, which is not
  included in the final package metadata, but is used at build-time to check
  availability of at least one provider; you can specify that with `!` after
  the dependency, e.g. `cmd:sed!bsdsed`. In a lot of cases dependencies are
  automatic, and you should not specify any dependencies that would already
  be covered by the scanner. When using version constraints, any apk-style
  version pattern is allowed, such as `N<V`, `N<=V`, `N=V`, `N>V`, `N>=V`
  as well as fuzzy patterns `N~V` (e.g. `foo~3.0` will match `3.0.1`).
  The list may also contain package or subpackage objects, which get resolved
  to their fully versioned name, i.e. `pkg.pkgname_ver`.
* `env` *(dict)* Environment variables to be exported when running commands
  within the sandbox. This is considered last, so it overrides any possible
  values that may be exported by other means. Use sparingly.
* `exec_wrappers` *(list)* A list of 2-tuples specifying extra wrappers to
  set up for the build. The first element of the tuple is the full path to
  the program to wrap, while the second element is the wrapper name. You
  can use this to e.g. use `gsed` as `sed` by wrapping `/usr/bin/gsed`, in
  case it is too much trouble to patch the build system.
* `file_modes` *(dict)* A dictionary of strings to 3-tuples or 4-tuples,
  where the string keys are file paths (relative to the package, e.g.
  `usr/foo`) and the tuples contain user name, group name, permissions
  and optionally the recursive flag (`True` or `False`). The third field
  is a regular permissions integer, e.g. `0o755`. This can be used when
  the package creates a new group or user and needs to have files that
  are owned by that. The permissions are applied in the order the
  fields are added in the dictionary. Note that all setuid/setgid files
  as well as files with xattrs in the security namespace must have an
  explicit mode set here, otherwise they will not be allowed. That means
  any suid file installed by a package without the template re-declaring
  its mode is forbidden; the primary purpose is to make sure the packager
  knows what kind of mode it needs to have. This field can also be used
  to create empty directories in the package (bypassing the cleanup system),
  by specifying the path as starting with a plus (`+`). The mode and owner
  is still applied to the directory. If you require a user/group that does
  not exist in the environment by default, you can ensure it is created by
  putting a file called `sysusers.conf` in the template directory, containing
  configuration with the `sysusers(5)` syntax.
* `file_xattrs` *(dict)* A dictionary of strings to dictionaries, where
  the string keys are file paths (relative to the package, e.g. `usr/foo`)
  and the dicts contain mappings of extended attribute names to values.
  The values can be strings, which are then passed to `setfattr`, or they
  can be `None`, which will erase any existing extended attribute of that
  name on the file. Currently it is not possible to preserve extended
  attributes set by package build, but they are tracked, i.e. for any
  already existing extended attribute you have to choose to either erase
  it or replace it with an explicit value, or the package build will
  fail. The `security.capability` attribute is treated specially and does
  not use `setfattr` but `setcap` instead. For extended attributes to work
  here, you need to have the right host programs (`setfattr` or `setcap`)
  installed in the package build environment via `hostmakedepends`.
  If setting the security namespace, `file_modes` entry must also be
  declared, see above.
* `hardening` *(list)* Hardening options to be enabled or disabled for the
  template. Refer to the hardening section for more information. This is
  a list of strings that works similarly to `options`, with `!`
  disabling the hardening options. Any enabled hardening option that is
  not supported by the target will be ignored.
* `hostmakedepends` *(list)* A list of strings specifying package names to
  be installed in the build container before building. These are always
  installed in the build container itself rather than target sysroot,
  even if cross compiling. Typically contains runnable tools. This is
  not installed during stage 0 bootstrap, since they come from the host.
* `ignore_shlibs` *(list)* A list of shared libraries (`NEEDED` values)
  to ignore in runtime dependency scan.
* `install_if` *(list)* A list of package names or version constraints that
  must be satisfied in order for this package to auto-install (i.e. if
  all packages in this list are installed, this one will also be installed).
  This is basically the reverse of a "recommends" feature. You should always
  include at least one versioned constraint. May contain actual package or
  subpackage objects, which resolve to their full versioned name like in
  the `depends` list.
* `make_cmd` *(str)* The name of the program used for building. May not
  apply to all templates or build styles. By default this is `make`.
* `make_env` *(dict)* Environment variables to be exported when running
  some build stage. For `make`, the call site `env` is most significant,
  followed by phase-specific `make` environment, followed by this, followed
  by global environment (`env`).
* `make_build_args` *(list)* A list of custom arguments passed to `make_cmd`
  during the build phase.
* `make_build_env` *(dict)* Environment variables to be exported when running
  the `build` phase. For `make`, the call site `env` is most significant,
  followed by this, followed by the rest.
* `make_build_target` *(str)* The `make_cmd` target to be used to build.
  Different build systems may use this differently. Empty by default.
* `make_build_wrapper` *(list)* A list of arguments to prepend before the `make`
  command during `build`. It is the middle wrapper, i.e. passed after the
  explicit one, but before `make_wrapper`.
* `make_check_args` *(list)* A list of custom arguments passed to `make_cmd`
  when running tests.
* `make_check_env` *(dict)* Environment variables to be exported when running
  the `check` phase. For `make`, the call site `env` is most significant,
  followed by this, followed by the rest.
* `make_check_target` *(str)* The `make_cmd` target to be used to run tests.
  Different build systems may use this differently (`check` by default
  unless overridden by the `build_style`).
* `make_check_wrapper` *(list)* A list of arguments to prepend before the `make`
  command during `check`. It is the middle wrapper, i.e. passed after the
  explicit one, but before `make_wrapper`.
* `make_dir` *(str)* The subdirectory of `cwd` that `make_cmd` is invoked in
  by default. This has the default value of `.`, so it normally does not
  impose any directory changes. However, the default may be altered by
  build styles. This is utilized by build systems such as `meson` and
  `cmake` to build outside the regular tree. It is also utilized by their
  `configure` steps as the working directory.
* `make_install_args` *(list)* A list of custom arguments passed to `make_cmd`
  when installing.
* `make_install_env` *(dict)* Environment variables to be exported when running
  the `install` phase. For `make`, the call site `env` is most significant,
  followed by this, followed by the rest.
* `make_install_target` *(str)* The `make_cmd` target to be used to install.
  Different build systems may use this differently (`install` by default).
* `make_install_wrapper` *(list)* A list of arguments to prepend before the `make`
  command during `install`. It is the middle wrapper, i.e. passed after the
  explicit one, but before `make_wrapper`.
* `make_wrapper` *(list)* A list of arguments to prepend before the `make`
  command. It is the least important wrapper, i.e. passed the last out of
  all wrappers.
* `makedepends` *(list)* A list of strings specifying package names to be
  installed in the build container. When cross compiling, these are installed
  into the target architecture sysroot. When not cross compiling, this is
  concatenated with `hostmakedepends`.
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
* `origin` *(str)* This can be optionally specified and it's a package
  name (without a version). Normally, the origin for primary package is
  itself, and for subpackage it's its primary package. This can be overridden
  for instance when what would normally be a subpackage is split off into
  a separate template. It primarily affects the implicit replaces behavior
  related to other packages of the same origin. It inherits into subpackages.
  The primary use for this is to give all "defaults" packages providing
  alternative program symlinks the same origin so they can replace each other
  freely without errors.
* `prepare_after_patch` *(bool)* Normally, the `prepare` phase is run before
  the `patch` phase so that vendored dependencies can be patched. Sometimes
  it is necessary to patch lockfiles/dependency lists though and then it may
  be necessary to run `prepare` after that is done.
* `provider_priority` *(int)* The final tie-breaker when choosing between
  two virtual providers to install. When everything else fails (i.e. version
  is the same and so on), the provider with the higher priority is chosen.
  Defaults to 0.
* `provides` *(list)* A list of packages provided virtually, specified
  in the format `foo=1.0-r0`. The package manager will consider these
  alternative names for the package, and automatically have them
  conflict with other packages of this name. If the version part is
  not provided, several packages of that name may be installed, but
  none of them will be considered by default; instead, an error message
  will be given and the user will need to choose. Additionally, it can
  be used to provide `pc` files (like `pc:foo=1.0`, you can use `0` as
  a version fallback) and commands (like `cmd:foo`). This is notably
  useful when combined with the `!scanpkgconf` option and so on.
  It can also be used to provide extra shared libraries. This needs
  to be versioned with the full version of the shared library (you can
  infer that from the filename, e.g. `so:libfoo.so.1=1.4.2` when you have
  `libfoo.so.1` `SONAME` and full name `libfoo.so.1.4.2`). You can likewise
  use `0` as a fallback there. Typically, you will not use this as the shared
  library scanning is automatic; but sometimes libraries provide either a
  non-conforming `SONAME` which the scanner does not pick up, or the
  scanner is disabled explicitly.
* `renames` *(list)* A list of old names for the package. This is like
  `provides` except no explicit version is required (it always takes on
  the version of the package by default, but an explicit version can be
  specified if needed) and they always make it into autosplit packages
  with the appropriate suffix. This ensures a clean rename upgrade path.
* `replaces_priority` *(int)* When used with `replaces`, this specifies
  which of the packages gets to keep the files (i.e. the higher-priority
  package will keep them). Defaults to 0.
* `replaces` *(list)* A list of packages we are replacing, in the same
  constraint format as `provides`. This allows the current package to
  replace files of the listed packages, without complaining about file
  conflicts. The files from the current package will take over the
  conflicting files. This is primarily useful for moving files from one
  package to another, or together with `replaces_priority`, for "policy
  packages".
* `restricted` *(str)* By default, `cbuild` does not allow packages that
  are marked this way to be built. The value is the reason why it's marked
  like that. Often this will be e.g. non-redistributable clause in the
  terms of the package.
* `sha256` *(list or str)* A list of SHA256 checksums (or just one checksum
  as a string) specified as digest strings corresponding to each field in
  `source`. Used for verification.
* `skip_dependencies` *(list)* A list of relative patterns (may be globbed)
  that are matched when scanning dependencies (does not matter which type).
  Any file in the package matching any of the patterns is skipped for the
  purpose of dependendency scan (whether it's shared library dependencies,
  service dependencies, or anything). For practicality this is inherited
  into automatic subpackages (e.g. `-dinit`).
* `skip_providers` *(list)* A list of relative patterns (may be globbed) that
  are matched when scanning providers (does not matter which type). Any file
  in the package matching any of the patterns is skipped for the purpose of
  being a provider (e.g. matched shared libraries will not emit `so:` providers
  and so on). For practicality this is inherited into automatic subpackages
  (e.g. `-dinit`).
* `source` *(list or str)* A list of URLs to download and extract (by default).
  If there is only one source, this can be one string, which is equivalent to
  having a list with the string. Prefixing the string with `!` will prevent
  the extraction of the source. The rest of the string must be a URL. The
  resulting filename will normally be extracted from the URL by finding the
  last forward slash (The filename follows the slash). If `>` is present in
  the string later than a `/`, the filename instead follows the `>` and
  the `>` with the filename is stripped from the URL before download. This
  can be useful in cases where the URL does not have an obvious filename,
  or when the filename is ambiguous.
* `source_headers` *(list)* This must be a list that has as many entries as
  there are sources. Each item is a dict specifying name-value mappings of
  extra request headers to use when fetching. When it's not a list, it must
  be a dict; this is a shorthand when there is only one source (i.e. a dict
  is equivalent to a list of 1 dict).
* `source_paths` *(list)* This must be a list that has as many entries as
  there are sources. Each item is a string specifying a path within the
  `wrksrc` that the source's extracted result will have. Specifying an empty
  string or `.` implies default behavior. Effectively all sources that have
  a path that is not the default will be extracted separately and then moved
  into place.
* `subdesc` *(str)* The package sub-description which will be appended to
  the main description as ` (subdesc)`.
* `tools` *(dict)* This can be used to override default tools. Refer to the
  section about tools for more information.
* `tool_flags` *(dict)* This can be used to override things such as `CFLAGS`
  or `LDFLAGS`. Refer to the section about tools and tool flags for more
  information.
* `triggers` *(list)* A list of directory paths the package should trigger
  on. That is, if any package changes these monitored directories, the
  trigger script for this package should run. This can include wildcards
  (`foo/*` will fire on any directory inside `foo`).

Additionally, there is a variety of variables that are not generic but rather
are used by specific build styles. They are listed and described in each
build style's section.

<a id="template_functions"></a>
### Template Functions

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
use up to 4 functions - `init_PHASE`, `pre_PHASE`, `PHASE` and `post_PHASE`.
They are called in that order. The `pre_` and `post_` functions exist so that
the template can specify additional logic for when the main function is
already defined by a `build_style`.

The `init_` prefixed function is, unlike the other 3, not subject to stamp
checking. That means it is called every time, even during repeated builds,
which is useful as the template handle is persistent - once data is written
in it, it will last all the way to the end, so you can use the `init_` hooks
to initialize data that later phases depend on, even if the phase itself is
not invoked during this run (e.g. when re-running build after a failure).

The phases for which all this applies are `fetch`, `extract`, `prepare`,
`patch`, `configure`, `build`, `check` and `install`. They are invoked
in this order.

Every other function defined in template scope is not used by `cbuild`.
However, all regular names are reserved for future expansion. If you want
to define custom functions (e.g. helpers) in template scope, prefix their
names with an underscore.

Also keep in mind that the order of execution also interacts with hooks.
See the section on hooks for more information.

<a id="arch_patterns"></a>
### Architecture Patterns

A template can specify which architectures it can build for. The `archs`
meta field is used for that and has roughly this format:

```
archs = ["pat1", "pat2", ...]
```

A concrete example would be something like this:

```
archs = ["x86_64", "ppc*", "riscv*", "!arm*"]
```

This would specify that the template can build on the `x86_64` architecture
as well as any architecture matching `ppc*` or `riscv*`, but never on any
architecture matching `arm*`.

The syntax follows usual shell-style "glob" rules. That means supporting
the `*`, `?`, `[seq]` and `[!seq]` patterns (the matching is implemented
using the `fnmatch` case-sensitive pattern matcher in Python). In addition
to that, `!` in front of the pattern can negate it.

When not specified, it's the same as specifying `*` as the sole pattern.

The system checks the list for all matching patterns. The most strictly
matching pattern trumps everything, with "most strictly" meaning matching
the largest number of exact characters; all pattern styles are considered
equally "loose", so `foo*z` is equally strict to `foo[xy]z`. It is an
error if you have two matching equally strict patterns, as well as if you
have two identical patterns but only one is negating.

If the finally picked pattern is negating or if no matching pattern was
found in the list, the template is considered not buildable.

<a id="build_styles"></a>
### Build Styles

Build styles are a way to simplify the template by inserting pre-defined
logic with a single line.

```
build_style = "meson"
```

With this, you declare that this template uses the Meson build
system. What actually happens is that the build style will create some
of the necessary functions (`build` etc) implicitly.

A build style is a Python file in `cbuild/build_style` and looks like
this:

```
def configure(self):
    pass

def build(self):
    pass

def install(self):
    pass

def use(tmpl):
    tmpl.configure = configure
    tmpl.build = build
    tmpl.install = install

    tmpl.build_style_defaults = [
        ("make_cmd", "mything")
    ]
```

The template can further override pieces of the build style as necessary,
while the build style can set any functions it wants. It can also define
new template variables, as well as override default values for any
template variable.

In general, build styles are small wrappers over the `cbuild.util`
namespace APIs. That allows you to use the APIs when you need logic that
cannot be declared with just a simple variable, and keep templates simple
where that is sufficient.

There are currently a few build styles available.

#### meta

A metapackage `build_style`. It merely defines empty `fetch` as well
as `install`. Packages with this build-style are allowed to be empty
by default, others need to use the `empty` option.

#### cargo

You generally use this one for Rust projects.

**NOTE:** this build style will be subject to major changes in the future.

Sets `prepare`, `build`, `check`, `install`. They are wrappers
around the `cargo` utility module API.

By default, environment will be updated for all invocations to set up
the Cargo environment variables for the current target as well as various
common environment variables to devendor system libraries.

The `self.make_dir` variable is used as the working source directory. Other
variables of interest are `self.make_build_args`, `self.make_build_env`,
`self.make_build_wrapper`, and equivalents for other build phases, as those
are used to pass things to Cargo.

The `prepare` step is run with network access and pre-vendors all crates
into the tree. That allows for easy patching (vendor checksums need to be
cleared afterwards using the utility API). The rest of the build is run
with network access disabled.

When `cargo-auditable` is available, all commands will implicitly be run
through the `auditable` wrapper.

#### cmake

You can generally use this for CMake-using projects.

Variables:

* `cmake_dir` A directory relative to `cwd` of the template that contains
  the root `CMakeLists.txt`. By default it is `None`, which means that it
  is directly in `cwd`.

Default values:

* `make_cmd` = `ninja`
* `make_check_target` = ``
* `make_dir` = `build`

Sets `configure`, `build`, `check`, `install`. They are wrappers
around the `cmake` utility module API `configure`, `build`, `install`,
and `ctest` respectively.

The `self.make_dir` value is passed as `build_dir`. The `self.configure_args`,
`self.make_build_args`, `self.make_check_args`, `self.make_install_args` values
are passed as extra arguments. The given environments are made up of the values
of `self.make_env` (for every step besides `configure`) combined with the
values of `self.configure_env`, `self.make_build_env`, `self.make_check_env`,
`self.make_install_env`. Wrappers are allowed for everything but `configure`,
using the combination of `self.make_wrapper` with `self.make_build_wrapper`,
`self.make_check_wrapper` and `self.make_install_wrapper`.

The `ctest` API is used for `check` when `self.make_check_target` is default. If
it's set to a value, it's taken as a hint not to use `ctest` and instead use
`build` with `--target` set to `self.make_check_target` in extra arguments.

When `self.make_build_target` is set to a value, it is passed as `--target`
as an extra argument to `build`.

The `self.make_cmd` value determines the generator. If kept as `ninja`, the
Ninja generator will be used during `configure`. Otherwise, `Unix Makefiles`
generator will be used.

Note these variables are passed by the build style only, and manual `cmake`
invocations do not receive them.

#### configure

A simple style that runs `self.configure_script` within `self.chroot_cwd`
with `self.configure_args` for `configure` and uses a simple `Make` from
`cbuild.util` to build.

Sets `configure`, `build`, `check`, `install`.

You are expected to supply all other logic yourself. This build style works
best when you need a simple, unassuming wrapper for projects using custom
configure scripts. For `autotools` and `autotools`-compatible systems, use
`gnu_configure`.

Additionally creates `self.make`, which is an instance of `cbuild.util.make.Make`
for the template, with no other changes.

#### gnu_configure

A more comprehensive `build_style`, written around `cbuild.util.gnu_configure`.

Default values:

* `make_dir` = `build`
* `configure_gen` = `["autoreconf", "-if", "-W", "none"]`

Sets `configure`, `build`, `check`, `install`.

During `configure`, `gnu_configure.replace_guess` is called first, followed
by `gnu_configure.configure`. The `configure` script is run inside `self.make_dir`.

Additionally creates `self.make`, which is an instance of `cbuild.util.make.Make`
for the template, with `build` `wrksrc`, and `env` retrieved using the
`gnu_configure.get_make_env` API.

All of this means that `gnu_configure` can implicitly deal with cross-compiling
and other things, while `configure` can't.

Autodetects `slibtool` and makes it used via `rlibtool` and `slibtoolize`.
It is recommended to include `slibtool` in `hostmakedepends` instead of
`libtool` if the build process does not break due to it.

#### go

You generally use this one for Go projects.

**NOTE:** this build style will be subject to major changes in the future.

Variables:

* `go_mod_dl` (`mod`) May be set to `mod` or `off` to control module downloads.
* `go_build_tags` Optional list of tags to use for build.
* `go_check_tags` Optional list of tags to use for check.

Default values:

* `make_dir` = `build`

Sets `prepare`, `build`, `check`, `install`. They are wrappers
around the `golang` utility module API.

By default, environment will be updated for all invocations to set up
the Go environment variables for the current target. These include
`GOMODCACHE` (to save files in the cbuild cache), `GOARCH` (and maybe
`GOARM`) and `CGO_CFLAGS`, `CGO_CXXFLAGS`, and `CGO_LDFLAGS`.

The `prepare` step is run with network access and caches the module swith
`go mod download` by default, unless `vendor` directory already exists.
If it exists, it may be forced by setting `go_mod_dl`.

The build is performed with `go build`. By default, `-o {make_dir}/` is passed
to it alongside any `make_build_args`. The `-trimpath` argument is used by
default as well.

For installation, the `go` command is not used. Instead, `make_dir` is globbed
for `**/*` and found files are installed as binaries. Some projects will
want to override this.

Check has `./...` passed unless `make_check_args` is provided. The `go test`
command is used.

#### makefile

A wrapper around `cbuild.util.make`.

Variables:

* `make_use_env` A boolean (defaults to `False`) specifying whether some of the
  core variables will be provided solely via the environment. If false, they
  are also provided on the command line. These variables are `OBJCOPY`, `RANLIB`,
  `CXX`, `CPP`, `CC`, `LD`, `AR`, `AS`, `CFLAGS`, `FFLAGS`, `LDFLAGS`, `CXXFLAGS`
  and `OBJDUMP` (the last one only when not bootstrapping) during `build`.
  All of these inherently exist in the environment, so if this is `True`, they
  will not be passed on the command line arguments.

Sets `configure`, `build`, `check`, `install`.

The `install` target is always called with `STRIP=true` and `PREFIX=/usr`.

Additionally creates `self.make`, which is an instance of `cbuild.util.make.Make`
for the template, with no other changes.

#### meson

You can use this for Meson-using projects.

Variables:

* `meson_dir` A directory relative to `cwd` of the template that contains
  the root `meson.build`. By default it is `None`, which means that it
  is directly in `cwd`.

Default values:

* `make_build_target` = `all`
* `make_dir` = `build`
* `make_cmd` = `ninja`

Sets `configure`, `build`, `check`, `install`. They are wrappers
around the `meson` utility module API `configure`, `install`, and `test`, except
`build`, which calls `self.make_cmd` (with the right number of jobs).

The `self.make_dir` value is passed as `build_dir`. The `self.configure_args`,
`self.make_build_args`, `self.make_check_args`, `self.make_install_args` values
are passed as extra arguments. The `self.make_build_target` is also passed and
usually should not be user-set. The given environments are made up of the values
of `self.make_env` (for every step besides `configure`) combined with the
values of `self.configure_env`, `self.make_build_env`, `self.make_check_env`,
`self.make_install_env`. Wrappers are allowed for everything but `configure`,
using the combination of `self.make_wrapper` with `self.make_build_wrapper`,
`self.make_check_wrapper` and `self.make_install_wrapper`.

During build, `meson-test-prereq` is also unconditionally passed in the build
targets to ensure all test prerequisites are built. There should never be a need
to override this.

Note these are passed by the build style only, and manual `meson` invocations
do not receive them.

#### python_pep517

A build style for Python modules (PEP517). Requires to have `python-build`
and `python-installer` in `hostmakedepends`, along with the build backend
of your choice.

Default values:

* `make_build_target` = `.`
* `make_check_target` =
* `make_install_target` = `dist/*.whl`

Sets `build`, `check`, `install`.

The `build` builds a wheel with `python -m build`. The `install` will
install the contents of the wheel. The `check` will run `pytest` or fail.

The `make_install_target` is used as a glob pattern to match built wheels.

<a id="subpackages"></a>
### Subpackages

The `cbuild` system has support for subpackages. Subpackages are
regular packages repository-wise, except they are built as a part of
some main package's process, and are created from its files.

Subpackages are used for a variety of things, such as separating
development files from the main package, or for plugins.

You should create a symbolic link named like the subpackage in the respective
repo category and have it point to the directory with the main package template.

In the template file, you use a decorator. The decorator is available globally
during the time a package is initialized. The syntax works like this:

```
@subpackage("mysubpackage")
def _(self):
    ...
```

The function name must be a single underscore. The subpackage name follows the
same conventions as the main package (notably, it must be lowercase). In order
to cover more cases, the subpackage definition can also be conditional:

```
@subpackage("mysubpackage", foo == bar)
def ...
```

The subpackage will only be defined if the condition argument is `True`.
**Note that this is the only way subpackages should ever be conditional in.**
Generally it applies that if the subpackage symlink exists in `cports`, there
should always be a decorated subpackage function. The reason for this is that
`cbuild` should be aware of any subpackage the template may generate, without
regard to whether it will be generated or not. This is useful as it allows
for better introspection/analysis by tooling.

The subpackage body function can look like this:

```
@subpackage("foo-devel")
def _(self):
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

Any list entries that start with a question mark, e.g. `"?usr/foo"`, are
optional (i.e. that path may be missing). This is useful for programatically
generated subpackages (when multiple subpackages are generated from some kind
of input list and they share the general layout but not the exact contents).

They may also start with `@`, in which case a symlink will be created. The
string must be in the format `@path=>target`, e.g. `@usr/bin/foo=>bar`. The
special delimiter `=>` is not allowed in the path.

The `self` argument here is the subpackage handle.

If better control over the files is needed, you can also return a function
instead of a variable. The function takes no arguments (you are supposed
to nest this function and refer to the subpackage via its parent function)
and can use `self.take(path)` and the likes.

The following variables apply to subpackages. Most do not inherit their
value from the parent and are assigned the defaults; some are inherited,
those are explicitly marked.

* `pkgdesc` (inherits)
* `options`
* `depends`
* `provides`
* `nostrip_files`
* `hardening`
* `nopie_files`
* `file_modes`
* `shlib_provides`
* `shlib_requires`
* `triggers`

The `hardening` option does not actually do anything (since subpackages do
not affect the build) and its sole purpose is to be able to turn off the PIE
check for subpackages (as projects may build a mixture of PIE and non-PIE
files).

The subpackage may gain an implicit `subdesc` if its name has a certain suffix:

* For `-devel`, it will be `development files`
* For `-static`, it will be `static libraries`
* For `-libs`, it will be `libraries`
* For `-progs`, it will be `programs`

You should never make suffixes a part of `pkgdesc`. The suffix is replaced on
per subpackage basis.

There are also automatic subpackages, which can be declared explicitly if
needed, and those have their own descriptions as well. See the later section
of this document for those.

In general, subpackage descriptions should have suffixes like that. You can
choose the best suffix for packages not matching standardized names. Sometimes
it may also be the case a `-devel` subpackage corresponds to another subpackage
rather than the main package, and the default description will thus be wrong.
In those cases, you should override it while following the conventions.

Additionally, `depends` is special for subpackages. If the subpackage is a
`-doc` or `-dbg` subpackage, it will by default gain a dependency on their
parent (i.e. unprefixed) package automatically. If you want to add more
dependencies, you can append. If you do not want the parent package
dependency, e.g. when the package is special and does not have a parent,
you can just overwrite it. For `foo-static`, the base dependency is `foo-devel`.

If any broken symlink in a package or subpackage resolves to another subpackage
or the main package, a dependency is automatically emitted - see the section
about automatic dependencies below.

#### Automatic subpackages

There are subpackages that are generated automatically.

These are (with their package description suffixes):

* `dbg` - `(debug files)`
* `doc` - `(documentation)`
* `man` - `(manual pages)`
* `dinit` - `(service files)`
* `dinit-links` - `(service links)`
* `initramfs-tools` - `(initramfs scripts)`
* `udev` - `(udev rules)`
* `bashcomp` - `(bash completions)`
* `zshcomp` - `(zsh completions)`
* `fishcomp` - `(fish completions)`
* `nucomp` - `(nushell completions)`
* `locale` - `(locale data)`
* `static` - `(static libraries)`
* `pycache` - `(Python bytecode)`

These suffixes should be considered reserved, i.e. you should not make a
package with the reserved suffix unless it's replacing the otherwise
automatic subpackage, and they themselves should not split off any further
subpackages.

They are split off based on existence of certain files inside the package,
except debug packages, which are split off if any debug information could
be stripped off ELF files within the package.

Automatic subpackages are automatically installed under certain circumstances,
except for debug and static packages. For automatic installation to happen,
the package they were split off needs to be installed, plus the following:

* `base-doc` for `-doc` subpackages
* `base-man` for `-man` subpackages
* `base-udev` for `-udev` subpackages
* `base-locale` for `-locale` subpackages
* `base-devel-static` for `-static` subpackages
* `dinit-chimera` for `-dinit` subpackages
* the `-dinit` subpackage for `-dinit-links` subpackages
* `initramfs-tools` for `-initramfs-tools` subpackages
* `bash-completion` for `-bashcomp` packages
* `zsh` for `-zshcomp` packages
* `fish-shell` for `-fishcomp` packages
* `nushell` for `-nucomp` packages
* `python-pycache` for `-pycache` packages (except `python-pycache` itself)

Development packages may be automatically installed if `base-devel` is
installed and specific other circumstances enable this. Please refer to
the section about automatic dependencies below.

You can turn off automatic splitting with the `!autosplit` option. Some
templates also have builtin whitelists for split subpackage data, e.g.
`eudev` will not split off a `-udev` subpackage.

You can turn on/off splitting only static libraries with `splitstatic`.

<a id="automatic_deps"></a>
### Automatic Dependencies

The build system includes an automatic dependency scanner. This allows you
to deal with a lot of what you would ordinarily need to specify by hand.

Packages are scanned for the following:

1) What they provide
2) What they depend on

Packages can automatically provide:

1) Shared libraries (`.so` files)
2) `pkg-config` definitions (`.pc` files)
3) Commands (executables)

Packages can automatically depend on:

1) Shared libraries
2) `pkg-config` definitions
3) Symbolic link providers

First, packages are scanned for their shared library dependencies. This is
done by recursively scanning the package tree for ELF files and inspecting
their `NEEDED`. This will result in a `SONAME`. This `SONAME` is then
matched against providers among installed packages. That means providers
must be installed as `makedepends`.

If a provider is not found, the system will error. Of course, things that
are provided within the package are skipped. Likewise, if a dependency is
found in a subpackage of the current build, it is used directly and not
scanned within repositories.

Shared libraries without `SONAME` can still participate in the resolution
if they exist directly in `usr/lib` and do not have a suffix beyond `.so`.

During stage 0 bootstrap, the repository is considered in addition to
already installed packages. This is because we do not have a full build
root at this point, and lots of things are instead provided from the
host system at that point.

Once shared libraries are dealt with, the package is scanned for `.pc`
files. Each `.pc` file is inspected for their `Requires` (public as well
as private) and dependencies are automatically added as `pc:` dependencies
into the resulting `apk`. These can be version constrained, the version
constraint is preserved. The `.pc` files may exist in `usr/lib/pkgconfig`
and `usr/share/pkgconfig` and nowhere else.

Of course, if the `.pc` file exists within the same package, no dependency
is added. All `pc:` dependencies that are added are reverse-scanned for
their providers in the repository (an exception to this is if the `pc:`
dependency exists in a subpackage). If no provider can be located, the
system will error.

Lastly, symlink dependencies are scanned. If a broken symlink is encountered
somewhere in the package, the system will try to resolve it to files in
other subpackages of the same set. If found, a dependency will be added,
this dependency is versioned (since all subpackages share a version).
This is mostly useful so that `-devel` packages can automatically depend
on whatever they correspond to (since `-devel` packages contain `.so`
symlinks, which resolve to real files in the runtime package).

Broken symlinks that do not resolve to anything are normally an error. You
can override it by putting `brokenlinks` in `options`, or better, using
the `broken_symlinks` template field.

Once dependencies are scanned, the package is scanned for provides, so
that other packages can depend on it.

ELF files with a suffix starting with `.so` are considered for `so:`
provides. Files with just a `.so` suffix participate in this if they exist
directly in `usr/lib` (as otherwise they may be e.g. plugins and we do
not want to handle those). Versioned files (e.g. `.so.1`) can be located
anywhere. If the version contains anything that is not a number, it is
skipped.

Eligible files are scanned for `SONAME` information. If they do not provide
one, the library is skipped. If they provide an unversioned `SONAME` (i.e.
one that ends with `.so`) they are skipped when not directly in `/usr/lib`.
The filename is scanned for version. For example, `libfoo.so.1.2.3` with
`SONAME` `libfoo.so.1` will provide a `so:libfoo.so.1=1.2.3`. If no version
is provided in the filename, `0` is used. If a version is found, it must
validate as an `apk` version number.

The package is then scanned for `.pc` files to be provided. Only two paths
are considered, `usr/lib/pkgconfig` and `usr/share/pkgconfig`. IT is an error
for the same `.pc` file to exist in both paths. The `.pc` files are scanned
for version (this version is sanitized, any `-(alpha|beta|rc|pre)` has its
dash replaced with an underscore to be compliant, and the result is verified
with `apk`). If no version information is present, `0` is used by default.
For `foo.pc`, The provide will become `pc:foo=VER`.

Lastly, the package is scanned for command provides. Every file in `usr/bin`
is a command, and will make a `cmd:foo` for `usr/bin/foo`.

There are some `options` you can use to control this. With `!scanrundeps`,
no dependencies will be scanned. As for provides, that can be controlled
with `scanshlibs`, `scanpkgconf`, `scancmd`, and `scanservices`.

#### Development packages and install_if

There is a mechanism in place that lets development subpackages (those that
end with `-devel`) to be automatically installed. In order for that to
happen, the `base-devel` package needs to be installed in the system,
in addition to a specific set of packages.

The behavior of this may be overridden by the packager by disabling the
`scandevelif` subpackage option. Defining a custom non-empty `install_if`
list will likewise automatically disable this behavior entirely.

The dependencies of the subpackage are scanned, and if any full local
dependencies are present (i.e. to another subpackage or the main package,
and fully versioned), this dependency is added to the `install_if`. That
allows the package to be autoinstalled if enabled by policy *and* if
the non-development packages are already installed.

For static libraries, the mechanism is a little different, as they are
usually split off automatically and a hook cannot be used. They get their
install_if against their base development package, in addition to the
`base-devel-static` policy package. If this does not work for something,
for example if the relationship is reversed or the base package does not
exist, it is possible to set `install_if` to an empty array in the
subpackage definition.

<a id="template_options"></a>
### Template Options

There are various options you can specify as a part of the `options` variable.
Some of them can only be specified at the top level, while some also apply
to subpackages.

The following options are toplevel-only, i.e. they apply globally within
the template including for subpackages:

* `bootstrap` *(false)* This option specifies that the template is built
  during bootstrapping. Other templates will fail to build unless a build
  container is available.
* `parallel` *(true)* By disabling this, you can enforce single-threaded
  builds for the template. By default the number of build jobs passed
  by `cbuild` is respected. Note that this does not influence LTO linker
  threads.
* `debug` *(true)* By default, debug packages (`-dbg`) are generated if
  there are any strippable debug symbols. By setting this to `false`,
  you can disable passing of debug options to the compiler, as well as
  prevent generation of debug packages.
* `check` *(true)* By disabling this you can ensure the `check` phase
  is never run, even if enabled and enforced in the build system. A
  reason should always be provided as a comment above the `options`
  field.
* `checkroot` *(false)* You can use this to run the `check` stage as
  root. This is useful for some test suites that will not function
  otherwise. Of course, this still uses namespaces, so it does not
  actually run as your host system root (as it can't).
* `installroot` *(true)* By default, install phase is run as `root`.
  This is done with `fakeroot`, which may interfere with rpath if
  such binary is invoked during installation. You may disable this
  in those cases. For stage 0 builds, it is always disabled.
* `cross` *(true)* If disabled, the template will error early when
  attempting cross compilation.
* `lint` *(true)* If enabled, the template contents will be checked
  for additional errors before building. This includes correct ordering
  of fields, validation of URL and description strings and other checks.
  It does not check formatting of the template, as that can be handled
  better with external tools.
* `relr` *(true)* If enabled, DT_RELR will be used for smaller size.
  This can be safely applied almost everywhere, but e.g. not for the
  libc. Enabling it means requirement of at least musl 1.2.4.
* `lto` *(true)* If enabled, LTO will be used. This will result in the
  necessary compiled flags being applied. Build styles can alter their
  behavior to accommodate the flags. The default LTO type is thin LTO,
  which can be overridden with `ltofull`.
* `ltofull` *(false)* If you set this together with `lto`, full LTO will
  be used. It does not activate LTO by itself.
* `linkparallel` *(true)* Similarly to `parallel`, this can be used to
  disable linker and LTO threads.
* `linkundefver` *(false)* Pass `--undefined-version` to `ld.lld` to
  bypass version errors in affected packages.
* `framepointer` *(true)* If enabled, frame pointers will be turned
  on to make profiling of resultant binaries easier.
* `fullrustflags` *(false)* If enabled, RUSTFLAGS will also contain
  the same optimisation flags that are normally set for cargo only.
* `sanruntime` *(false)* If enabled, the full sanitizer runtime will
  be linked in and the code will be compiled without trapping. This allows
  for better diagnostics for debugging hardening issues, but should not
  be used in final packages.

The following options apply to a single package and need to be specified
for subpackages separately if needed:

* `textrels` *(false)* By default, if `cbuild` finds textrels within any
  ELF files in the packages, it will error. It is possible to override
  this by enabling the option.
* `execstack` *(false)* By default, if `cbuild` finds ELF files with
  executable stack, it will error. It is possible to override this by
  enabling the option. Any ELF file that either does not have `PT_GNU_STACK`
  or has the `1 << 0` bit set in its `flags`.
* `foreignelf` *(false)* By default, if `cbuild` finds ELF files that
  have a foreign machine architecture (checked by matching against the
  `libc` of the target), it will error. It is possible to override this
  by enabling this option. Usually this is a wrong thing to do, but for
  example in case of cross toolchains you might want to enable this.
* `empty` *(false)* By default, empty packages will raise an error, unless
  the build style is `meta`; this can be used to override it. Packages that
  are marked empty and have contents will instead error then.
* `keepempty` *(false)* By default, `cbuild` will prune all empty directories
  from every package. This can be used to override that. It should almost
  never be used. However, there are some cases, notably `base-files`, where
  keeping empty directories is intended. In most cases, when an empty directory
  is desired, a placeholder file called `.empty` should be created in it, which
  ensures that users cannot accidentally `rmdir` the directory.
* `keeplibtool` *(false)* By default, `cbuild` will remove libtool `.la` files
  everywhere. This lets you preserve them in specific rare cases.
* `brokenlinks` *(false)* By default, broken symlinks that cannot be resolved
  within any subpackage will result in an error. You can override this behavior
  but usually shouldn't. It's generally better to use the `broken_symlinks`
  pattern list to restrict the set.
* `hardlinks` *(false)* Normally, multiple hardlinks are detected and errored
  on. By enabling this, you allow packages with hardlinks to build.
* `lintcomp` *(true)* If enabled, shell completion commands get checked to see
  if they resolve to a matching command.
* `lintstatic` *(true)* Normally, static libraries are not allowed to be in
  the main package. In specific rare cases, this may be overridden.
* `lintpixmaps` *(true)* Normally, the `/usr/share/pixmaps` path is not
  allowed as it's frequently used for application icons that should go in
  `/usr/share/icons/hicolor` (typically in scalable and bitmap versions).
  However, some packages use it privately and not for standard application
  icons, so it may be disabled.
* `scantrigdeps` *(true)* This specifies whether trigger dependencies should
  be scanned. See the `src/cbuild/hooks/pre_pkg/007_trigger_deps.py` for
  detailed list.
* `scanrundeps` *(true)* This specifies whether automatic runtime dependencies
  are scanned for the package. By default, ELF files are scanned for their
  dependencies, which is usually desirable, but not always.
* `scanshlibs` *(true)* If disabled, the package will not be scanned for
  shared libraries to be provided by the package.
* `scanpkgconf` *(true)* If disabled, the package will not be scanned for
  `.pc` files.
* `scanservices` *(true)* If disabled, the package will not be scanned for
  service files.
* `scandevelif` *(true)* If disabled, `install_if` will not be generated
  for development packages.
* `scancmd` *(true)* If disabled, the package will not be scanned for
  executable commands.
* `spdx` *(true)* If enabled, the license name(s) will be validated
  as SPDX compliant. License for subpackages is validated separately,
  if overridden (if not overridden, validation is skipped).
* `distlicense` *(true)* If the license of the package needs distribution,
  verify that the license file is being distributed. Keep in mind that the
  linter may not be exhaustive as the SPDX license data do not specify
  whether a license should be distributed or not.
* `strip` *(true)* If disabled, ELF files in this package will not be
  stripped, which means debug symbols will remain where thesy are and
  debug package will not be generated.
* `ltostrip` *(false)* By default, `lto` being enabled disables stripping
  of static archives, as LTO archives consist of bitcode and not object
  files. You can enforce the pass to run with this, which is mainly useful
  for when there are mixed LTO and non-LTO archives or when something is
  built with GCC and `-ffat-lto-objects`. Keep in mind that you will have
  to use `nostrip_files` to filter out bitcode archives with this option.
* `autosplit` *(true)* If disabled, the build system will not autosplit
  subpackages (other than `-dbg`, which is controlled with other vars).
* `splitstatic` *(false, true)* This is like `autosplit`, but only for
  static libraries. It is on by default for `devel` packages and off
  otherwise. You can change the default by toggling this.
* `splitudev` *(true)* This is like `autosplit`, but only for udev
  rules.
* `splitdinit` *(true)* This is like `autosplit`, but only for dinit
  service files and links.
* `splitdoc` *(true)* This is like `autosplit`, but only for docs.

<a id="hardening_options"></a>
### Hardening Options

The `cbuild` system implements an automatic way to deal with toggling
different hardening options. Several hardening options are implicit
as a part of our toolchain and do not have toggleable options; those
include FORTIFY and RELRO.

Currently the following options are always enabled by default:

* `pie` Position-independent executables.
* `ssp` Enables `-fstack-protector-strong`.
* `scp` Enables `-fstack-clash-protection` (`ppc64le`, `ppc64`, `ppc`, `x86_64`)
* `int` Traps signed integer overflows and integer division by zero.
* `format` Format-security default errors for C and C++ (compile-time).
* `var-init` Auto-zero initialization for variables (`-ftrivial-auto-var-init=zero`)

Several others are available that are not on by default:

* `vis` Build with `-fvisibility=hidden` in default flags.
* `cfi` Enables Clang Control Flow Integrity (needs `vis`, `x86_64` and `aarch64`)
* `sst` Enables Clang SafeStack (`x86_64`, `aarch64`)

Hardening options that are not supported on a platform are silently disabled,
but their dependency relationships are always checked.

CFI should be enabled where possible. Our current CFI is not cross-DSO, which
means calls across shared library boundaries will not be checked, and the whole
template needs building with hidden visibility. A lot of projects do not like
being built with hidden visibility, and since Clang CFI is type-based, it is
rather easy to encounter CFI violations, so it is not something that can just
be enabled and expected to work. Careful testing should be done for each template
that enables CFI.

The `int` hardening option is enabled by default, but can likewise result in
crashes in various programs/libraries. However, such crashes are always bugs
in those programs/libraries. The best solution is to fix the issues and submit
patches upstream, but in case of complicated bugs, it is okay to disable it in
the template and put in a comment for later (with information on how to reproduce
the crash).

<a id="tools"></a>
### Tools and Tool Flags

The build system also provides separate management of tools for convenience.
Similarly, it allows you to declare custom tool flags. Tools and tool flags
in this case refer primarily to the toolchain and flags passed to it.

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

The following tool flags are defined:

* `CFLAGS` (C)
* `CXXFLAGS` (C++)
* `FFLAGS` (Fortran)
* `LDFLAGS` (linker, usually passed together with one of the above)
* `RUSTFLAGS` (Rust)

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
their host values, as `BUILD_CC`, `BUILD_LD` and so on, as well as GNU-style
`CC_FOR_BUILD` and the likes. This is to ensure that project build systems
can utilize both host and target toolchains where appropriate.

Tool flags have a bit more elaborate handling. Similarly to tools they
are also exported into the environment by their names, including for
the host profile with the `BUILD_` prefix. However, the actual values
are composed of multiple parts, which are generally the following:

1) Any hardening flags for the tool as defined by current `hardening` of the
   template, possibly extended or overridden by the `hardening` argument.
2) The flags as defined in either the current build profile or `target`.
3) Bootstrapping or cross-compiling flags.
4) The flags as defined in your template, if any.
5) `-ffile-prefix-map={chroot_srcdir}=.` to improve ccache behavior
   for `CFLAGS` and `CXXFLAGS`.
6) Any extra flags from `extra_flags`.
7) Debug flags as corresponding to the tool according to the current debug
   level (default or template-specified), if building with debug.

Not all of the above may apply to all tool types, but it tends to apply to
compilers. Any differences will be noted in here, if needed.

There are many more variables that are implicitly exported into the
environment, but those are documented elsewhere.

<a id="triggers"></a>
### Triggers

The packaging system lets you provide custom triggers.

Triggers are scripts that run if something modifies a monitored directory.
Each package is allowed to carry one trigger script, and this trigger must
have a list of directory patterns set up for it. These directory patterns
are then monitored for changes, potentially by other packages. That means
other packages can result in invocation of triggers even if the package
providing the trigger is not modified in any way.

Triggers are fired when the affected directory is modified in any
way, this includes uninstallation.

The script is provided as a file in the template's directory,
named `pkgname.scriptname`, e.g. `foo.trigger`.

If a trigger script is provided, the `triggers` variable must be set
appropriately.

Triggers are passed the directory paths that resulted in the trigger
being invoked.

<a id="build_profiles"></a>
## Build Profiles

The `cbuild` system allows for flexible definition of profiles for
different target architectures. These profiles are used for both
native and cross builds.

The definition exists in `etc/build_profiles/ARCH.ini` where `ARCH`
is the `apk` architecture name (in general matching `uname -m`).

It may look like this:

```
[profile]
endian    = little
wordsize  = 64
triplet   = riscv64-unknown-linux-musl
machine   = riscv64
goarch    = riscv64
repos     = main
[flags]
CFLAGS    = -march=rv64gc -mabi=lp64d
CXXFLAGS  = ${CFLAGS}
FFLAGS    = ${CFLAGS}
LDFLAGS   =
RUSTFLAGS =
```

These are also the fields it has to define. The `triplet` must always
be the full triplet (`cbuild` will take care of building the short
triplet from it if needed). The compiler flags are optional.

The `repos` field specifies which categories are provided by remote
repositories. As different architectures may provide different
package sets and some architectures don't have remote repositories
at all, this is specified in the profile as we have no way to check
it (and assuming all repos exist would just lead to needless failures
when updating the package indexes).

There is also the special `bootstrap` profile used when bootstrapping.
It differs from normal profiles in that the `profile` section is not
actually specified, as the endianness and word size are already known
from the host and the rest of the info is architecture specific. What
it can specify is the `flags` section, and possibly also additional
per-architecture flags (e.g. `flags.riscv64`). User specified flags
from global config are ignored when bootstrapping.

The `cbuild` system provides special API to manipulate profiles, and
you can utilize any arbitrary profiles within one build if needed.
More about that in the respective API sections, but the API allows
one to retrieve compiler flags in proper architecture-specific way,
check if we are cross-compiling and otherwise inspect the target.

API-side, the profile (retrieved with `self.profile()` for example)
is represented as a `Profile` object. It looks like this:

```
class Profile:
    arch = ...
    triplet = ...
    short_triplet = ...
    machine = ...
    sysroot = ...
    wordsize = ...
    endian = ...
    cross = ...
    repos = ...
    goarch = ...
    goarm = ...
```

The properties have the following meanings:

* `arch` The `apk` architecture name of the profile.
* `triplet` The "long" target triplet (e.g. `aarch64-unknown-linux-musl`)
* `short_triplet` The "short" target triplet (e.g. `aarch64-linux-musl`)
* `machine` The `uname` machine of the profile. Matches `arch` if not explicit.
* `sysroot` A `pathlib` path representing the sysroot.
* `wordsize` The integer word size of the target (typically 64 or 32).
* `endian` The endianness of the target (`little` or `big`).
* `cross` A boolean that is `True` for cross compiling targets and
  `False` otherwise.
* `goarch` The architecture name for the Go programming language. Optional
  and only present when supported by the toolchain.
* `goarm` For 32-bit ARM (`goarch` is `arm`) this is the ARM architecture
  version (ARMv5/6/7).

For the `bootstrap` profile, `triplet` and `short_triplet` are `None`.

The `sysroot` refers to `/` for native targets and `/usr/<short_triplet>` for
cross-compiling targets.

In general, you will not want to use the profile's methods, and the member
variables are strictly read only.

<a id="build_environment"></a>
## Build Environment

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

When bootstrapping the build container from binary packages,
`/etc/machine-id` is generated as a random string. This is mainly
to allow things that need it to pass tests and so on.

The following environment variables are exported into the sandbox:

* `PATH` The executable path, includes `/usr/bin` plus possible
  additions for `ccache` and so on.
* `SHELL` Set to `/bin/sh`.
* `HOME` Set to `/tmp`.
* `LC_COLLATE` Set to `C`.
* `LANG` Set to `en_US.UTF-8`.
* `UNAME_m` Set to the preferred host architecture. Read by `uname(1)`.
* `PYTHONUNBUFFERED` Set to `1`. This disables output buffering on
  Python subprocesses, which allows output to be printed right away,
  since `cbuild` captures it for logging purposes.
* `SOURCE_DATE_EPOCH` The timestamp for reproducible builds.
* `CBUILD_STATEDIR` Points to where current package build metadata
  is stored, such as stamps for finished phases.
* `CFLAGS` Target C compiler flags.
* `FFLAGS` Target Fortran compiler flags.
* `CXXFLAGS` Target C++ compiler flags.
* `LDFLAGS` Target linker flags.
* `RUSTFLAGS` Target Rust compiler flags.
* `CC` Target C compiler.
* `CXX` Target C++ compiler.
* `CPP` Target C preprocessor.
* `LD` Target linker.
* `PKG_CONFIG` Target `pkg-config`.
* `STRIPBIN` Set to a special wrapper that avoids stripping the file.
  This is in order to bypass `install(1)` `-s` argument.
* `CBUILD_TARGET_MACHINE` Target `apk` machine architecture.
* `CBUILD_TARGET_TRIPLET` Full target triplet (as described in profile).
  This is not exported during stage0 bootstrap.
* `CBUILD_TARGET_SYSROOT` Target sysroot path. Host sysroot is always `/`.
* `BUILD_CFLAGS` Host C compiler flags.
* `BUILD_FFLAGS` Host Fortran compiler flags.
* `BUILD_CXXFLAGS` Host C++ compiler flags.
* `BUILD_LDFLAGS` Host linker flags.
* `BUILD_RUSTFLAGS` Host Rust compiler flags.
* `BUILD_CC` Host C compiler.
* `BUILD_CXX` Host C++ compiler.
* `BUILD_CPP` Host C preprocessor.
* `BUILD_LD` Host linker.
* `BUILD_PKG_CONFIG` Host `pkg-config`.
* `CBUILD_HOST_MACHINE` Host `apk` machine architecture.
* `CBUILD_HOST_TRIPLET` Full host triplet (as described in profile).
  This is not exported during stage0 bootstrap.

All `BUILD_foo` variables are also exported as `foo_FOR_BUILD`.

Additionally, when using `ccache`, the following are also exported:

* `CCACHEPATH` The path to `ccache` toolchain symlinks.
* `CCACHE_DIR` The path to `ccache` data.
* `CCACHE_BASEDIR` Set to the `cbuild`-set current working directory.
* `CCACHE_TEMPDIR` Set to `/tmp/ccache`.

When using `sccache` and it is installed, the following are exported:

* `RUSTC_WRAPPER` Set to `/usr/bin/sccache`.
* `SCCACHE_DIR` The path to the `sccache` data.
* `SCCACHE_IDLE_TIMEOUT` Set to 30 by default.

When set in host environment, the variables `NO_PROXY`, `FTP_PROXY`,
`HTTP_PROXY`, `HTTPS_PROXY`, `SOCKS_PROXY`, `FTP_RETRIES`, `HTTP_PROXY_AUTH`
are carried over into the environment.

The values of the `tools` meta variable are also exported. Additionally,
values of the `env` meta variable are exported, taking priority over any
other values. Finally, when invoking code in the sandbox, the user of the
API may specify additional custom environment variables, which further
override the rest.

The container is entered with a specific current working directory. At first
this is `self.srcdir`, then from `configure` onwards it may enter `build_wrksrc`
if set (which is inside `self.srcdir`). This applies to all parts of each
phase, including `init`, `pre` and `post`.

The current working directory may be overridden locally via API, either for
the template or for the specific container invocation.

The following bind mounts are provided:

* `/` The root, read-only.
* `/ccache` The `ccache` data path (`CCACHE_DIR`), read-write.
* `/builddir` The directory in which `self.srcdir` exists.
* `/destdir` The destination directory for installing; packages will
  install into `/destdir/pkgname-pkgver`, or when cross compiling,
  into `/destdir/triplet/pkgname-pkgver`. Read only before `install`,
  and read-write for the `install` phase.
* `/sources` Read-only, points to where all sources are stored.
* `/dev`, `/proc` and `/tmp` are fresh (not bound).

The bind mount names are not guaranteed so templates are not supposed to
rely on them; use the proper variables.

Once the `fetch` phase is done, all possible namespaces are unshared.
This includes the network namespace, so there is no more network
access within the sandbox at this point.

<a id="hooks"></a>
## Hooks and Invocation

The `cbuild` system is largely driven by hooks. A hook is a Python source
file present in `cbuild/hooks/<section>`. Hooks take care of things such
as sources handling, environment setup, linting, cleanups, and so on. Some
things are hardcoded within `cbuild` and not done by hooks.

The following hook types are allowed:

* `fetch` (default fetch code)
* `extract` (default extract code)
* `prepare` (bldroot tree preparation)
* `setup` (build environment preparation)
* `patch` (default patch code)
* `destdir` (final tree preparation per-subpackage, may change it)
* `pkg` (final state preparation + lint, may no longer change destdir)

Hooks are stamp-checked, except `setup`, which is run always. They are
typically called together with the corresponding phase functions, but not
always. Every hook defined in the section directory is invoked, in sorted
order, so they use numerical prefixes to ensure sorting.

A hook looks like this:

```
def invoke(pkg):
    pass
```

It takes a package (sometimes this may be a subpackage) and does not return
a value, though it may error.

This is the overall call order of hooks and phases:

* `init_fetch` (template, always)
* `pre_fetch` (template)
* `fetch` (template if defined, otherwise hooks)
* `post_fetch` (template)
* `init_extract` (template, always)
* `pre_extract` (template)
* `extract` (template if defined, otherwise hooks)
* `post_extract` (template)
* `init_patch` (template, always)
* `pre_patch` (template)
* `patch` (template if defined, otherwise hooks)
* `post_patch` (template)
* `init_prepare` (template, always)
* `pre_prepare`, `prepare`, `post_prepare` (template)
* `setup` (hooks, always)
* `init_configure` (template, always)
* `pre_configure`, `configure`, `post_configure` (template)
* `init_build` (template, always)
* `pre_build`, `build`, `post_build` (template)
* `init_check` (template, always)
* `pre_check`, `check`, `post_check` (template)
* `init_install` (template, always)
* `pre_install`, `install`, `post_install` (template)
* `pkg_install` (subpackage, each) and `destdir` (hooks, each subpackage)
* `destdir` (hooks, for main package)
* `pkg` (hooks, for each subpackage)

After the `pkg` hooks, packages are generated and registered.

<a id="custom_targets"></a>
### Custom Targets

It is possible to define custom target functions like so:

```
@custom_target("my-target", "configure")
def _(self):
    ...
```

This can then be invoked like `./cbuild invoke-custom my-target main/mypkg`.
The second argument specifies which regular packaging steps have to run before
running this.

Custom targets do not emit/capture log files so they can be used for things
that require interactivity. The primary purpose is to provide logic
for things like bindist generation for toolchain bootstrapping and so on.

You can query the current target at template toplevel, e.g. to add extra
dependencies:

```
if self.current_target == "custom:my-target":
    hostmakedepends += ...
```

<a id="staging"></a>
## Staging

The build system implements staging. This means packages do not get registered
into the actual final repo outright, but instead they first get staged and
only when ready, they get moved into the repository proper.

Every built package gets staged first. There is a specific staging overlay
repo for every repository, but the unstaging algorithm considers them all
a single global stage.

When you invoke a build (`./cbuild pkg category/foo`), it must first finish.
This includes building potential missing dependencies. Once the entire
potential batch is built, the unstaging algorithm kicks in and does the
following:

1) If the user has explicitly requested that the package remains staged,
   nothing is done. This can be done via a command line option to `cbuild`
   or using the configuration file.
2) The system collects all staging overlays currently present.
3) Every staging overlay is searched for packages. These packages are
   collected and each package is checked for its virtual providers. These
   include shared libraries (`so:libfoo.so=ver`) and others. The system
   checks both the staged version and a possible previously built version
   that was already built and not in stage. The providers of both are
   collected.
4) Staged version providers are accumulated in the `added` global set.
   The previous version providers are in the `dropped` global set. This
   happens only if the providers between the versions differ. If they
   do, the package is considered `replaced`.
5) Common entries between `added` and `dropped` are eliminated. These
   are entries that have the same name as well as version.
6) Now all `dropped` providers are searched for in both the main repos
   and the stages. Their reverse dependencies (i.e. things depending on
   them) are collected, and each reverse dependency is stored in a global
   set.
7) Each reverse dependency is searched for and its dependencies are collected.
   Only the "best" version is considered, which is the potentially staged
   one. Every dependency is checked if it matches something in the `dropped`
   set. Version constraints are respected here. If one is not found in the
   `dropped` set, the dependency is discarded. Otherwise, it is added into
   a set of dependencies for further checking.
8) Each revdep dependency that satisfied a `dropped` provider is further
   checked for providers. If a provider that was not `replaced` is found,
   then the dependency is discarded. This ensures that if there is another
   provider that can satisfy the dependency, we don't have to worry about it.
9) If the resulting set is empty, the repository gets unstaged as there
   is nothing else to consider. If it is not empty, the repositories are
   kept staged, and a list of packages depending on each problematic
   provider is printed.

This algorithm is not perfect and will not catch certain edge cases, such as
when moving a provider from `main` to `user` but there still being packages
that depend on it in `main`. This is an intended tradeoff to keep things
reasonably simple. You are expected to be careful with such cases and deal
with them properly.

The main point of the staging system is to handle `soname` updates in a way
that does not disrupt user workflow. That is, when a `soname` is increased
for a library, the rebuild will get staged until everything depending on
it has been rebuilt against the new version too. While the package system
deals with this gracefully and would not let users update affected packages,
it is better to make this invisible and keep the old versions until things
are ready.

Additionally, it is there for convenience, to be notified of potential
rebuilds to be done, as well as so one does not forget.

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

#### self

Using `self`, you can access the `Template` handle from the global scope.
Keep in mind that at this point, it is uninitialized - not even things run
during the `init()` call are set up.

Also, do not rely on it inside functions. Its existence is limited to the
time when the primary template body is being executed. Of course, functions
in general take the handle as the first argument, which is by convention
also called `self`. You can obviously rely on that, just do not rely on it
being implicitly defined.

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

Filesystem APIs take strings or `pathlib` paths. They also allow the special
prefix `>/` in the path as a shorthand for `self.destdir`, and the special
prefix `^/` that is a shorthand for `self.files_path`.

##### self.pkgname

A string representing the name of the package.

##### self.full_pkgname

A string in the format `repository/pkgname`.

##### self.pkgver

The version number of the package. While provided as a template variable,
this is inherited into subpackages as well, so it's considered a part of
the base API.

##### self.pkgrel

The release number of the package. While provided as a template variable,
this is inherited into subpackages as well, so it's considered a part of
the base API.

##### self.full_pkgver

The full version in format `pkgver-rpkgrel`. It is available even on the
top level after the respective package fields are set.

##### self.pkgname_ver

A string like `pkgname=full_pkgver`. Useful for exact dependencies.

##### def with_pkgver(self, name)

Build a string like `{name}={self.full_pkgver}`.

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

##### self.chroot_statedir

Same as `statedir`, but when viewed from inside the sandbox.

##### def log(self, msg, end = "\n")

Using `self.logger.out()`, print out a specially prefixed message. The
message has the format `<prefix>: <msg><end>`, where `prefix` can be
one of the following:

* `{self.pkgname}-{self.pkgver}-r{self.pkgrel}`
* `{self.pkgname}`
* `cbuild`

This depends on the stage of the build.

##### def log_red(self, msg, end = "\n")

Like `log`, but using `out_red`.

##### def log_warn(self, msg, end = "\n")

Like `log`, but using `warn`.

##### def error(self, msg, end = "\n")

In addition to logging a message like `log_red`, also raises an error,
which will abort the build.

##### def pushd(self, dirn, glob = False)

To be used as a context manager. Temporarily changes the `cwd` as well
as `chroot_cwd` of the template to point to `dirn` (which is treated
as a relative path to current `cwd`).

This is pretty much an equivalent of the Unix `pushd`/`popd` commands.

Usage:

```
with self.pushd("src"):
    pass
```

If you set `glob` to `True`, you may use wildcards in the given path.
The result must match exactly one path. You can use `**` to glob
recursively.

For example:

```
with self.pushd("build/*/foo", glob = True):
    pass
```

##### def cp(self, srcp, destp, recursive = False, symlinks = True, glob = False)

Copies `srcp` to `destp`. Both paths are considered potentially relative
to `cwd`. If `srcp` is a file, it is copied into `destp` if a directory,
or becomes `destp`. If `symlinks` is `True`, symlinks are followed, i.e.
if `srcp` was a symlink, the result will be a copy of the file it resolves
to.

If `srcp` is a directory, `recursive` must be `True` else the function
will error. This includes the case when `srcp` is a symbolic link to a
directory. In the latter case, `srcp` is copied as-is to `destp` like
if it was a file, and `symlinks` is ignored. The meaning of `symlinks`
is the opposite for directories with `recursive`, if it is `True`, all
symlinks are preserved, otherwise they are resolved.

If `glob` is `True`, `srcp` is first globbed and each matching path is
copied. There must be at least one match.

This mimics the behavior of the Unix `cp` tool.

##### def mv(self, srcp, destp, glob = False)

Moves `srcp` to `destp`. If `destp` is an existing directory, `srcp` is
moved into that directory, otherwise `srcp` is renamed to `destp`.
Both paths are considered potentially relative to `cwd`.

If `glob` is `True`, `srcp` is first globbed and each matching path is
copied. There must be at least one match.

This mimics the behavior of the Unix `mv` tool.

##### def mkdir(self, path, parents = False)

Creates the directory `path`. If `parents` is `False` and the parent of
`path` does not exist, this will error. If the directory already exists,
it will likewise error. If `parents` is `True`, it will create all parent
directories, and it will never error when `path` already exists and is
a directory.

Mimics the behavior of the Unix `mkdir` tool, possibly with `-p`.

##### def rm(self, path, recursive = False, force = False, glob = False):

Removes the path `path`. Can be either a file or a directory. If it is
a directory (symlinks are treated as files) and `recursive` is not `True`,
an error is raised. If `force` is `True`, the function will never error
when `path` is non-existent.

If `glob` is `True`, `path` is first globbed and each matching path is
copied. There must be at least one match.

Mimics the behavior of the Unix `rm` tool, `recursive` is like `-r` and
`force` is like `-f`.

##### def ln_s(self, srcp, destp, relative = False)

Creates a symlink at `destp` pointing to `srcp`. The `destp` is considered
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

This is a low level API. It should not be used for installation, you should
use `install_link` or `make_link` (or the `@` syntax) for that. It is, however,
useful to manipulate the local source tree in build steps.

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

##### def find(self, path, pattern, files = False)

Returns a generator object that represents a recursive search for `pattern`
within `path` (which is considered potentially relative to `cwd`). Each
result is a `pathlib.Path` object that is a found entry. If `files` is
set to `True`, only files are considered.

Usage:

```
for p in self.find("foo", "*.py"):
    ...
```

<a id="class_template"></a>
#### Template Class

APIs not available on subpackages.

##### self.conf_jobs

The number of configured jobs to use for building. This is not affected
by whether parallel builds are disabled via options, always referring
to the number provided by `cbuild`.

##### self.conf_link_threads

The number of linker threads (and LTO jobs, if enabled) to use. This is
not affected by whether parallel builds are disabled via options, always
referring to the number provided by `cbuild`.

##### self.make_jobs

The number of jobs to use for building. Unlike `conf_jobs`, this will always
be 1 if `parallel` option is disabled.

##### self.link_threads

The number of linker threads (and LTO jobs, if enabled) to use. Unlike
`conf_link_threads`, this will always be 1 if `linkparallel` option is disabled.

##### self.force_mode

Whether the build was forced (boolean).

##### self.stage

The current bootstrap stage. When `0`, it means we're running the first-stage
bootstrap that does not have a sandbox and runs on top of the host system.

During normal builds, it's `3`. During other stages of source bootstrap,
it can be `1` (when compiling using the sandbox generated by stage 0) or
`2` (when compiling using the sandbox generated by stage 1).

##### self.run_check

Whether running the `check` phase is enabled by `cbuild`. This is `False` for
cross builds even if testing is otherwise enabled. Keep in mind that setting
`!check` in `options` will not make this `False`, as it's set before options
are read.

You should never base your `makedepends` or `hostmakedepends` on whether you
are running tests or not. Packages should always be built with an identical
environment regardless of settings.

##### self.build_dbg

Whether building `dbg` packages is enabled by `cbuild`.

##### self.use_ccache

Whether using `ccache` is enabled by `cbuild`.

##### self.use_sccache

Whether using `sccache` is enabled by `cbuild`.

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

##### self.sources_path

The aboslute path to where the source files for the template are stored.

##### self.chroot_sources_path

Like `self.sources_path`, but within the sandbox for in-chroot operations.

##### self.bldroot_path

The absolute path to the `bldroot`.

##### self.srcdir

The absolute path to extracted source root, without accounting for things
like `build_wrksrc`.

##### self.chroot_srcdir

Like `srcdir`, but when viewed from inside the sandbox.

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

##### self.python_version, self.python_major, self.python_minor

These variables are available from `configure` stage onwards assuming Python
is available in the build root.

The `python_version` is a string (e.g. `3.12`) while the other two are integers
(e.g. 3 and 12).

##### self.ruby_version, self.ruby_major, self.ruby_minor, self.ruby_patch

Similar to Python above, but for Ruby.

##### def get_data(self, key, default = None)

Get a value assigned to a key from the global configuration's data section.
This is useful if you have e.g. some personal authentication token needed
to fetch particular sources, and you do not want to paste the token directly
to the template.

##### def do(self, cmd, *args, env = None, wrksrc = None, capture_output = False, stdout = None, stderr = None, input = None, check = True, allow_network = False, path = None, tmpfiles = None)

Execute a command in the build container, sandboxed. Does not spawn a shell,
instead directly runs `cmd`, passing it `*args`. You can use `env` to provide
extra environment variables in addition to the implied ones (see the build
environment section). The provided env vars override whatever builtin ones
the system sets up.

The `wrksrc` is relative to current `cwd` of the template. If not given, the
working directory will be the current `cwd` of the template itself. Note that
working directories are viewed from inside the sandbox, so when passing absolute
paths, you should use the `chroot_`-prefixed bases.

The level of sandboxing used depends on the current build phase. In all cases,
the root filesystem will be mounted read only, the `builddir` will be mutable
unless we're after `post_install`, the `destdir` will be immutable unless we
are at `install` phase, and all namespaces will be unshared (including network
namespace) unless we're at `fetch`.

The `allow_network` argument can be used to conditionally allow network access
but only during the `fetch`, `extract`, `prepare` and `patch` phases.

The `path` argument is an array that can specify additional executable paths
to prepend to the sandbox `PATH`. These will take priority over the default
`/usr/bin`.

If run during the `install` phase (or during the `check` phase when `checkroot`
is enabled in `options`), the command will be run masquerading as the `root`
user. This affects all things that use this API, e.g. `make` invocations.
This behavior is to better accommodate various build systems.

By default, failed runs will result in an exception being raised. You can
bypass that by setting `check` to `False`. Also, by default all output is
printed out without capturing it; using `capture_output` you can override
that if needed.

The `stdout` and `stderr` arguments work the same as for Python `subprocess.run`,
likewise with `input`.

The `tmpfiles` argument can be a list of `pathlib.Path` specifying host-filesystem
file paths to be bound into the sandbox in `/tmp`. The target filenames will be
the same as the source filenames.

The return value is the same as from Python `subprocess.run`. There you can
access the return code as well as possibly captured `stdout`.

Usage:

```
self.do("foo", "--arg1", "--arg2", wrksrc = "bar")
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

##### def profile(self, target = None)

If `target` is not given, returns the current profile, otherwise only
to be used as a context manager. Temporarily overrides the current build
profile to the given `target`, which can be a specific profile name (for
example `aarch64`) or the special aliases `host` and `target`, which refer
to the build machine and the target machine respectively (the target machine
is the same as build machine when not cross compiling).

It is also possible to specify `target:native` as well as e.g. `aarch64:native`
to force a non-cross profile in an environment where target would otherwise
be cross. This is useful for particular cases of compiler flags and so on.

Usage:

```
with self.profile("aarch64") as pf:
    ... do something that we need for aarch64 at the time ...

if self.profile().endian == "big":
    ...
```

##### def get_tool_flags(self, name, extra_flags = [], hardening = [], shell = False, target = None)

Get specific tool flags (e.g. `CFLAGS`) for the current profile or for `target`.

The `target` argument is the same as for `profile()`.

See the section on tools and tool flags for more information.

The return value will be a list of strings, unless `shell` is `True`, in
which case the result is a shell-escaped string that can be passed safely.

##### def get_cflags(self, extra_flags = [], hardening = [], shell = False, target = None)

A shortcut for `get_tool_flags` with `CFLAGS`.

##### def get_cxxflags(self, extra_flags = [], hardening = [], shell = False, target = None)

A shortcut for `get_tool_flags` with `CXXFLAGS`.

##### def get_fflags(self, extra_flags = [], hardening = [], shell = False, target = None)

A shortcut for `get_tool_flags` with `FFLAGS`.

##### def get_ldflags(self, extra_flags = [], hardening = [], shell = False, target = None)

A shortcut for `get_tool_flags` with `LDFLAGS`.

##### def get_tool(self, name, target = None)

Get the specific tool (e.g. `CC`) for the current profile or for `target`.

The `target` argument is the same as for `profile()`.

This properly deals with cross-compiling, taking care of adding the right
prefix where needed and so on. It should always be used instead of querying
the `tools` member variable directly.

##### def has_hardening(self, hname, target = None)

Check if the current configuration (i.e. taking into account the template
as well as the current profile or the `target`) has the given hardening
flag enabled. For a hardening flag to be enabled, it must not be disabled
by the template or defaults, and it must be supported for the target.

The `target` argument is the same as for `profile()`.

##### def has_lto(self, target = None, force = False)

Check if the current configuration (i.e. taking into account the template
as well as the current profile or the `target`) is going to LTO the
build. This will be `True` if the template does not disable it, and
if the stage is at least 2 and the profile supports it.

If `force` is set, then the `options` are ignored and only the profile
is checked for the current stage. This is useful for checks at template
level where options are not yet initialized, or for checking if LTO
is available for the profile regardless of whether disabled.

##### def can_lto(self, target = None)

Check if the current profile and stage can utilize LTO during builds.
Unlike `has_lto()`, it will still potentially return `True` even if
the template disables it in options.

This is useful for specific scenarios such as when the template disables
LTO but still uses it internally in the build system (e.g. toolchain
builds where LTO is only applied to the last stage).

##### def install_files(self, path, dest, symlinks = True, name = None)

Installs `path` (which may be a file or a directory and is relative
to `cwd` of the template) to `dest` (which must refer to a directory,
and must not be absolute - it is treated as relative to `destdir`).

If `name` is given, the installed source path will have that name.
Otherwise, the original name of the source path is preserved.

If `symlinks` is `True` (which is the default), symlinks in `path`
will also be symlinks in `dest`.

Usage:

```
self.install_files("data/foo", "usr/share")
```

##### def install_dir(self, dest, mode = 0o755)

Creates a directory `dest` in `destdir`.

Usage:

```
self.install_dir("usr/include")
```

##### def install_file(self, src, dest, mode = 0o644, name = None, glob = False, follow_symlinks = True, template = None, pattern = None)

Installs `src` into `dest`, where `src` refers to a file (absolute or
relative to `cwd`) and `dest` refers to a directory (must exist and be
relative).

The destination file must not already exist. The permissions are adjusted
to `mode`, unless set to `None`. The destination file name will be `name`,
unless it is `None`, in which case the source file name is kept.

The `dest` is created if non-existent.

If `glob` is set to `True`, the `src` must be a string specifying a relative
glob pattern to `self.cwd` and `name` must not be specified. In this case,
multiple files may be installed, but at least one must be matched.

If `template` is a dictionary, the source file will be searched for `pattern`,
which is implicitly `@(\w+)@` and if its capture matches any key in `template`,
will be substituted as a whole for the value in the dictionary. If a key does
not exist, it will be kept as is.

##### def install_bin(self, src, mode = 0o755, name = None, glob = False)

Equivalent to `self.install_file(src, "usr/bin", 0o755, name, glob)`.

##### def install_lib(self, src, mode = 0o755, name = None, glob = False)

Equivalent to `self.install_file(src, "usr/lib", 0o755, name, glob)`.

##### def install_man(self, src, name = None, cat = None, glob = False, lang = None)

Install a manpage `src`. That means installing the manpage into the right path
(`usr/share/man/manN` or when `lang` is specified, `usr/share/man/manN/{lang}`),
the category is automatically determined from the filename by default, but you
can specify it as `cat` (e.g. the integer `1`). The manpage will retain its
name, except when `name` is specified. This name should not include the
category (it is automatically appended, either as previously determined
from the filename, or as specified by `cat`).

The permissions will be `644`. All paths are created as necessary. The
`glob` argument is equivalent to `install_file`.

The input may be compressed, which is determined from whether it has the `.gz`
extension.

##### def install_license(self, src, name = None, pkgname = None)

Equivalent to `self.install_file(src, "usr/share/licenses/" + pkgname, 0o644, name)`.

##### def install_completion(self, src, shell, name = None)

Install a shell completion `src`. If not given, `name` will be expanded
to the package name. The `name` is the root of the completion file name
that will be adjusted according to the shell. The `shell` must be one of
`bash`, `zsh`, `fish`, `nushell`.

When `name` is not given, `self.pkgname` is used.

##### def install_service(self, src, name = None, enable = False)

If `src` is a file path that does not have the `.user` extension, it installs
the file in `usr/lib/dinit.d` with mode `0o644`. Otherwise, it installs the file
in `usr/lib/dinit.d/user` with its extension removed. If `name` is provided, it
is used as it is without changes.

If `enable` is `True`, the service will be implicitly enabled as system service.

##### def install_tmpfiles(self, src, name = None)

Install a configuration file in `/usr/lib/tmpfiles.d`. By default, take the
base name (plus `.conf` extension) from the package name, but that can be
overridden.

##### def install_sysusers(self, src, name = None)

Install a configuration file in `/usr/lib/sysusers.d`. By default, take the
base name (plus `.conf` extension) from the package name, but that can be
overridden.

##### def install_initramfs(self, src, stype = None, name = None)

Install an `initramfs-tools` hook or script. By default it installs a hook.
The hook/script will by default take the name of the package unless `name`
is explicitly provided. If `stype` (which should not be a named argument)
is unset or `hook`, it will be a hook; otherwise it will be installed under
the specified category in `scripts`, e.g. `init-top`.

##### def install_link(self, dest, tgt, absolute=False)

Creates a symbolic link at `dest`, pointing to `tgt`. The `tgt` should be
a relative target unless `absolute` is `True`.

Usage:

```
self.install_link("usr/lib/libfoo.so", "libfoo.so.1")
```

##### def install_shell(self, *args)

For each argument representing an absolute path to a shell, register it with
the system.

Usage:

```
self.install_shell("/usr/bin/bash")
```

##### def uninstall(self, path, glob = False)

Wipes the `path` (which must be a relative string) from the destination
directory. The path must match some files or directories. It can optionally
be globbed.

##### def rename(self, src, dest, relative = True, glob = False, keep_name = False)

Renames the `src` path (which must be a relative string) in the destination
directory to `dest`. The `dest` can be a relative path too. When `relative`
is true, something like `self.rename("foo/bar", "baz")` will make a `foo/baz`
while `self.rename("foo/bar", "bar/baz")` will make `foo/bar/baz`. When
it's false, the `dest` is treated as a separate new path within `destdir`,
so `self.rename("foo/bar", "bar/baz")` will make a `bar/baz`.

When `glob` is enabled, the `src` will be globbed beforehand and it must
return exactly one result. This is useful for fuzzy matches.

When `keep_name` is set, the original source name will be appended to the
final destination path, i.e. `self.rename("foo/bar", "baz", keep_name=True)`
becomes `foo/baz/bar`.

<a id="class_subpackage"></a>
#### Subpackage Class

These methods are only available on subpackage objects. You cannot create
a subpackage object directly, but it can be passed to hooks as well as
certain user defined functions.

Subpackage contents are taken explicitly from the main package. The only
contents that are taken implicitly are the potential licenses, i.e. the
`usr/share/licenses/<subpkgname>` path.

##### def take(self, p, missing_ok = False)

The subpackage will "steal" path `p`. The argument can be a string or
a `pathlib` path, representing a relative path to `destdir` of the main
package.

If `missing_ok` is `True`, the function will not error if the path does
not exist. In general you should not set this.

This additionally supports prefix-style shorthand values, e.g. instead
of `usr/bin/foo*` you can write `cmd:foo*`. The currently supported
prefixes are `cmd:`, `lib:` and `man:`; `man:` automatically resolves
the category, e.g. `man:foo.1` will take `usr/share/man/man1/foo.1`,
and `cmd:` will also take any associated manpage in either `man1` or `man8`
as well as known shell completions.

You will want to use this if you return a function from the subpackage
function. The following are equivalent:

```
def _(self):
    ...
    return ["usr/include", "usr/lib/*.a", "usr/lib/*.so"]

def _(self):
    ...
    def install():
        self.take("usr/include")
        self.take("usr/lib/*.a")
        self.take("usr/lib/*.so")

    return install
```

##### def take_devel(self, man = "23")

This function will `take` everything that should usually belong in a
development package. See the implementation in `cbuild/core/template.py`
for the current coverage.

Note that its handling of `.so` files in `/usr/lib` is a bit special; it will
only take symlinks, and files that are not ELF (in order to cover linker
scripts). Actual ELF files with raw `.so` suffix are skipped.

If `man` is a non-empty string, it represents the manpage categories to take.

##### def take_static(self)

This function will `take` everything that should usually belong in a
`-static` package. This is all static libraries in `usr/lib`.

##### def take_doc(self)

This function will `take` everything that should usually belong in a
documentation package. See the implementation in `cbuild/core/template.py`
for the current coverage.

##### def take_libs(self)

This function will `take` everything that should usually belong in a
`-libs` package. This is all shared libraries in `usr/lib` that start
with `lib` and follow a regular soname style. It also includes GObject
typelibs since those in general need to be available with the runtime
library for access from GI bindings.

##### def take_progs(self, man = "18")

This function will `take` everything that should usually belong in a
`-progs` package, i.e. all binaries in `usr/bin`.

If `man` is a non-empty string, it represents the manpage categories to take.

##### def default_devel(self, man = "23", extra = None)

A simple lazy wrapper around `take_devel` returning a function that you
should return from a subpackage (e.g. `return self.default_devel()`).

The `man` argument is passed as is to `take_devel`. The `extra` argument
can specify additional things to take. If `extra` is a `list`, each item
in the list is passed to `take()` (without any other arguments). Otherwise
it is considered a callable and called as is without argunents.

##### def default_static(self, extra = None)

A simple lazy wrapper around `take_static` returning a function that you
should return from a subpackage (e.g. `return self.default_static()`).

The `extra` argument can specify additional things to take. If `extra`
is a `list`, each item in the list is passed to `take()` (without any
other arguments). Otherwise it is considered a callable and called as
is without argunents.

##### def default_doc(self, extra = None)

A simple lazy wrapper around `take_doc` returning a function that you
should return from a subpackage (e.g. `return self.default_doc()`).

The `extra` argument can specify additional things to take. If `extra`
is a `list`, each item in the list is passed to `take()` (without any
other arguments). Otherwise it is considered a callable and called as
is without argunents.

##### def default_libs(self, extra = None)

A simple lazy wrapper around `take_libs` returning a function that you
should return from a subpackage (e.g. `return self.default_libs()`).

The `extra` argument can specify additional things to take. If `extra`
is a `list`, each item in the list is passed to `take()` (without any
other arguments). Otherwise it is considered a callable and called as
is without argunents.

##### def default_progs(self, man = "18", extra = None)

A simple lazy wrapper around `take_progs` returning a function that you
should return from a subpackage (e.g. `return self.default_progs()`).

The `man` argument is passed as is to `take_progs`. The `extra` argument
can specify additional things to take. If `extra` is a `list`, each item
in the list is passed to `take()` (without any other arguments). Otherwise
it is considered a callable and called as is without argunents.

##### def make_link(self, path, tgt)

A convenience wrapper around `self.ln_s`. Used to create symlinks, typically
for symlink provider packages. For example, to create a symlink `foo` in
`usr/bin` pointing to another binary called `bar`, you would do the following:

```
self.make_link("usr/bin/foo", "bar")
```

<a id="api_util"></a>
### Utility API

Utility APIs exist in the `cbuild.util` namespace. They provide building
blocks for templates, built using the other available public API. You do
not have to actually use any of these building blocks from technical
standpoint, but you are highly encouraged to use them in practice, as
they simplify the template logic greatly.

#### cbuild.util.cargo

Utilities for managing Cargo-based Rust projects.

##### def clear_vendor_checksums(pkg, crate, vendor_dir = "vendor")

Clears the file checksums in `.cargo-checksum.json` of a vendored crate.

You will need to do this for every crate you patch, as Cargo verifies the
checksums of every file specified in there. Clearing effectively allows
easy distro patching.

#### cbuild.util.cmake

A wrapper for management of CMake projects.

##### def configure(pkg, build_dir, cmake_dir = None, extra_args = [], env = {}, generator = None, cross_build = None)

Executes `cmake`. The directory for build files is `build_dir`, which
is relative to `chroot_cwd` (a good value is `build`). The root `CMakeLists.txt`
exists within `cmake_dir`, which is relative to `chroot_cwd` (when `None`, it
is assumed to be `.`).

The `pkg` is an instance of `Template`.

The `build_dir` is created if non-existent.

If `generator` is not set, it defaults to `Ninja`.

The arguments passed to `cmake` are in this order:

* `-G`
* `generator`
* `-DCMAKE_TOOLCHAIN_FILE=...`
* `-DCMAKE_INSTALL_PREFIX=/usr`,
* `-DCMAKE_BUILD_TYPE=None`,
* `-DCMAKE_INSTALL_LIBDIR=lib`,
* `-DCMAKE_INSTALL_SBINDIR=bin`,
* `extra_args`
* The directory for `cmake_dir`.

An appropriate toolchain file is created when bootstrapping and when cross
compiling. You can prevent the creation of a toolchain file by explicitly
setting `cross_build` to `False`. That will ensure a native-like build even
when the profile is set to a cross-compiling one.

The environment from `env` is used, being the most important, followed by
the rest.

##### def build(pkg, build_dir, extra_args = [], env = {}, wrapper = [])

Executes `cmake` with `--build` in `build_dir`. The `--parallel` argument
is passed with `pkg.make_jobs` alongside the given extra arguments. If a
wrapper is provided, it's executed through the wrapper.

##### def install(pkg, build_dir, extra_args = [], env = {}, wrapper = [])

Executes `cmake` with `--install` in `build_dir`. If a wrapper is provided,
it's executed through the wrapper. The `DESTDIR` variable is set in the default
environment.

##### def ctest(pkg, build_dir, extra_args = [], env = {}, wrapper = [])

Executes `ctest`. The directory for build files is `build_dir`.

The `pkg` is an instance of `Template`.

The command order is:

* `wrapper`
* `ctest`
* `extra_args`

The environment is taken from `env`, on top of default environment. The
`CTEST_PARALLEL_LEVEL` environment variable is by default set to the number
of jobs, and `CTEST_OUTPUT_ON_FAILURE` is set to `1`.

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

##### def configure(pkg, configure_dir = None, configure_args = None, configure_script = None, build_dir = None, extra_args = [], generator = None, env = {})

First, `build_dir` is created if non-existent (relative to `cwd`). If not
set, it is assumed to be `pkg.make_dir`.

If `generator` is `None`, it is taken from `pkg.configure_gen`. If it ends
up being non-empty, it is used as a command to generate the `configure_script`
and run in `cwd` with the same environment as the subsequent configure script.
Generally for `gnu_configure` build-styled templates, this will end up calling
`autoreconf -if -W none` unless overridden.

Then, the `configure_script` is called (which lives in `configure_dir`, by
default `.`, which lives in `chroot_cwd`, and its name is by default
`pkg.configure_script`).

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

The `configure_args` (`pkg.configure_args` if `None`) are passed after the implicit
args, finally followed by `extra_args`. Additionally, `env` is exported into the
environment, after the cache files (so the environment dictionary can override
any caches). This also uses `pkg.configure_env` (`env` takes precedence over it).

The environment variable `MAKE` is implicitly set for this run, with the value
of what the `cbuild.util.make.Make(pkg).get_command()` would be.

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

The `command` is the default `make` command. The `wrksrc` is relative to `cwd`.

###### def invoke(self, targets = [], args = [], jobs = None, env = {}, wrksrc = None, wrapper = [])

Invoke the tool, whose name is retrieved with `get_command()`. The
arguments are passed like this:

* `-jJOBS` where `JOBS` is `jobs` or `self.jobs` or `self.template.make_jobs`.
* `targets`, which can be a list of strings or a string, if a list all are
  passed, if a string the string is passed.
* `args`

The environment for the invocation works as follows:

* The most significant is `env`
* Then followed by `self.template.make_env`
* Then followed by the rest

The combined environment is passed to `self.template.do()`.

The `wrksrc` is either the `wrksrc` argument, `self.wrksrc`, or
`self.template.make_dir` in that order (the first that is set is used).

You can use this method as a completely generic, unspecialized invocation.

The `wrapper` is expanded before the command. You can use this to wrap `make`
invocations with different commands, e.g. when running tests.

###### def build(self, args = [], jobs = None, env = {}, wrksrc = None, wrapper = [])

Calls `invoke`. The `targets` is `self.template.make_build_target`, the
`args` are `self.template.make_build_args` plus any extra `args`. The
other arguments are passed as is.

The environment for the invocation works as follows:

* The most significant is `env`
* Then followed by `self.template.make_build_env`
* Then followed by `self.template.make_env`
* Then followed by the rest

###### def install(self, args = [], jobs = None, env = {}, default_args = True, args_use_env = False, wrksrc = None, wrapper = [])

Calls `invoke`. The `targets` is `self.template.make_install_target` and
`jobs`, `wrksrc` are passed as is.

If `default_args` is `True`, `DESTDIR` is passed implicitly (set to the
value of `self.chroot_destdir`. The method of passing it depends on the
value of `args_use_env`. If that is `True`, it is passed in the environment,
otherwise it is passed on the arguments (as the first argument).

The environment for the invocation works as follows:

* The most significant is `env`
* Then followed by `self.template.make_install_env`
* Then followed by `self.template.make_env`
* Then followed by a potential implicit `DESTDIR`
* Then followed by the rest

Other arguments that are passed as `self.template.make_install_args` plus
any extra `args`.

The `env` is passed as is, except when `DESTDIR` is passed via environment,
then it is passed together with that (user passed environment always takes
preference).

###### def check(self, args = [], jobs = None, env = {}, wrksrc = None, wrapper = [])

Calls `invoke`. The `targets` is `self.template.make_check_target`, the
`args` are `self.template.make_check_args` plus any extra `args`. The
other arguments are passed as is.

* The most significant is `env`
* Then followed by `self.template.make_check_env`
* Then followed by `self.template.make_env`
* Then followed by the rest

#### cbuild.util.meson

A wrapper for management of Meson projects.

##### def configure(pkg, build_dir, meson_dir = None, extra_args = [], env = {})

Executes `meson`. The `meson_dir` is where the root `meson.build` is located,
assumed to be `.` implicitly, relative to `chroot_cwd`. The `build_dir` is
the directory for build files, also relative to `chroot_cwd` (a good value
is `build`).

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
* `-Db_staticpic=true`
* `--cross-file=...` if cross-compiling
* `extra_args`
* `meson_dir`
* `build_dir`

When cross compiling, an appropriate cross file is automatically generated.

The environment from `env` is used, being the most important, followed by
the rest.

##### def invoke(pkg, command, build_dir, extra_args = [], env = {}, wrapper = [])

Generically invoke a `meson` command. This calls `meson`, giving it the command
and `extra_args`. If `wrapper` is given, `meson` is run through it. The given
`build_dir` is the working directory, and `env` is the environment.

##### def install(pkg, command, build_dir, extra_args = [], env = {}, wrapper = [])

Like running `invoke` with `install` command. The `DESTDIR` is passed via
the environment (any given `env` is of higher importance however). The
`--no-rebuild` flag is by default passed, followed by `extra_args`.

##### def test(pkg, command, build_dir, extra_args = [], env = {}, wrapper = [])

Like running `invoke` with `test` command. The `--no-rebuild` as well as
`--print-errorlogs` and `--num-processes` (with `pkg.make_jobs`) arguments
are passed, followed by any `extra_args`.

<a id="update_check"></a>
## Update Check

The system offers a way to check templates for updates. In a lot of cases,
especially for those using common hosting solutions, this is automatic and
there is no need to do anything.

You can invoke it like this:

```
$ ./cbuild update-check main/mypkg
```

This may have output like this, for example:

```
$ ./cbuild update-check main/llvm
llvm-12.0.0 -> llvm-12.0.1
llvm-12.0.0 -> llvm-13.0.0
```

If you pass an extra argument with any value, it will be verbose, printing
extra messages along the way.

The update checking can be tweaked by creating the file `update.py` in the
same directory with the template. This file is a Python source file
like the template itself, and likewise it can contain variables and hooks.

It can also reference the update check object via `self` at the global
scope. This can be used to retrieve data to process.

The allowed variables are:

* `pkgname` *(str)* This is the package name the default pattern checks
  for. By default, it is taken from the template. You can override this
  if the template name does not match the remote project name.
* `pkgver` *(str)* This is the version the fetched versions are compared
  against. You can use this when the version format of the package does
  not match and would result in wrong comparisons.
* `url` *(str)* The URL where the version numbers are mentioned. If unset,
  the `url` of the template (taken as is) plus the `source` URL(s) (with
  the filename component stripped) are used. An exception to this is when
  the `source` URLs contain `ftp.gnome.org`, in which case the `url` of
  the template is not used and only `source` URLs are.
* `pattern` *(str)* A Python regular expression (it is considered a verbose
  regular expression, so you can use multiple lines and comments) that
  matches the version number in the fetched page. You should match the
  version as accurately as possible, and use a capture for the version
  number itself, without the `pkgname` and so on. The `re.findall` API
  is used to search for it. There is a bunch of defaults that are applied
  for different known sites.
* `group` *(int)* The subgroup of the `pattern` match to use. You only
  need to use this if your pattern contains more than one capture group.
  If it contains just one, you should never use this.
* `ignore` *(list,bool)* A list of shell-style glob patterns that match
  version numbers ignored by the checker. You can use this to ignore
  for example beta versions. You can also set this to `True` to skip
  the update-check altogether. Packages with `meta` `build_style` are
  ignored automatically.
* `single_directory` *(bool)* You can set this to `True` if you wish to
  disable the default URL expansion logic. By default, for every collected
  URL, this looks for a versioned component in the path and if one is found,
  parent URL is fetched to figure out adjacent versioned URLs to consider
  for newer versions. This applies to projects that use source URLs such as
  `https://my.project/foo/foo-3.14/foo-3.14.tar.gz`. When this is unset,
  we can check the `foo` directory for versions. There are also various
  hosting sites that are explicitly blacklisted from the parent directory
  checks, since their specific URL is known (e.g. GitHub).
* `vdprefix` *(str)* A Python regular expression matching the part that
  precedes the numeric part of the version directory in the URL. Used when
  `single_directory` is disabled. The default is `|v|<pkgname>`.
* `vdsuffix` *(str)* A Python regular expression matching the part that
  follows the numeric part of the version directory in the URL. Used when
  `single_directory` is disabled. The default is `|\.x`.

You can define some functions:

* `collect_sources` A function taking the update check object, which is
  supposed to collect the initial list of source URLs to be considered.
  The default returns `self.collect_sources()`, which uses either
  `self.url` or `self.template.url` plus `self.template.source`.
* `expand_source` A function taking the update check object plus a URL
  (one for each returned from `collect_sources`). It is a filter function
  that returns a list (containing the input URL if it does not wish to
  expand or filter anything, and empty if it wishes to skip the URL). The
  default behavior is to return `self.expand_source(input)`, which
  returns the input when `single_directory` is set to `True` and does the
  parent directory expansion otherwise.
* `fetch_versions` A function taking the update check object plus a single
  URL and returning a list of version numbers. By default
  `self.fetch_versions(url)`.

These functions take the update check object. It has the following
properties:

* `verbose` Whether verbose logging is on.
* `template` The package template handle.
* `url`, `pkgname`, `single_directory`, `pattern`, `group`, `ignore`
  The variables.

It also has methods with the same names as the functions you can define.
You can call them from your custom functions.

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
