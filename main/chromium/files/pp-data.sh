#!/bin/sh

sed \
    -e 's/@@MENUNAME@@/Chromium/g' \
    -e 's/@@PACKAGE@@/chromium/g' \
    -e 's/@@USR_BIN_SYMLINK_NAME@@/chromium-browser/g' \
    chrome/app/resources/manpage.1.in > chromium.1


sed \
    -e 's/@@MENUNAME@@/Chromium/g' \
    -e 's/@@PACKAGE@@/chromium/g' \
    -e 's/@@USR_BIN_SYMLINK_NAME@@/chromium-browser/g' \
    -e 's/@@URI_SCHEME@@//' \
    -e '/@@EXTRA_DESKTOP_ENTRIES@@/d' \
    chrome/installer/linux/common/desktop.template > chromium.desktop

sed \
    -e 's/chromium-browser\.desktop/chromium.desktop/' \
    -e '/<update_contact>/d' \
    -e '/<p>/N;/<p>\n.*\(We invite\|Chromium supports Vorbis\)/,/<\/p>/d' \
    -e '/^<?xml/,$p' \
    chrome/installer/linux/common/appdata.xml.template \
    > chromium.appdata.xml
