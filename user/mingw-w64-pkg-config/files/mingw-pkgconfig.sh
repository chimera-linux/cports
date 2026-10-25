#!/bin/sh

# Taken from
# http://www.mega-nerd.com/erikd/Blog/CodeHacking/MinGWCross/pkg-config.html
# Thanks, Erik

# This file has no copyright assigned and is placed in the Public Domain.
# No warranty is given.

# When using the mingw32msvc cross compiler tools, the native Linux
# pkg-config executable works fine as long as the default PKG_CONFIG_LIBDIR
# is overridden.
export PKG_CONFIG_LIBDIR=/usr/x86_64-w64-mingw32/lib/pkgconfig

# Also want to override the standard user defined PKG_CONFIG_PATH with
# a mingw32msvc specific one.
export PKG_CONFIG_PATH=${PKG_CONFIG_PATH_CUSTOM}:${PKG_CONFIG_LIBDIR}

# Now just execute pkg-config with the given command line args.
pkg-config $@
