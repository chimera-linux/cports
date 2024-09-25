#!/bin/sh

_lib="$1"

echo "Removing buildscripts for system provided $_lib"
gfind . -type f -path "*third_party/$_lib/*" \
    \! -path "*third_party/$_lib/chromium/*" \
    \! -path "*third_party/$_lib/google/*" \
    \! -path './base/third_party/icu/*' \
    \! -path './third_party/libxml/*' \
    \! -path './third_party/pdfium/third_party/freetype/include/pstables.h' \
    \! -path './third_party/harfbuzz-ng/utils/hb_scoped.h' \
    \! -path './third_party/crashpad/crashpad/third_party/zlib/zlib_crashpad.h' \
    \! -regex '.*\.\(gn\|gni\|isolate\|py\)' \
    -delete
