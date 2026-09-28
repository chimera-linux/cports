#!/bin/sh

sed \
    -e 's/@@MENUNAME/Chromium/g' \
    -e 's/@@PACKAGE/chromium/g' \
    chrome/app/resources/manpage.1.in > chromium.1


sed \
    -e 's/@@MENUNAME/Chromium/g' \
    -e 's/@@PACKAGE/chromium/g' \
    -e 's/@@desktop_exec/chromium/g' \
    -e 's/@@desktop_icon/chromium/g' \
    -e 's/@@usr_bin_symlink_name/chromium-browser/g' \
    -e 's/@@uri_scheme//' \
    -e 's/@@startup_wm_class/Chromium/g' \
    -e '/@@extra_desktop_entries/d' \
    chrome/installer/linux/common/desktop.template > chromium.desktop

sed \
    -e 's/@@MENUNAME/Chromium/g' \
    -e 's/@@PACKAGE/chromium/g' \
    -e 's/@@SHORTDESC/Web browser/g' \
    -e 's/@@FULLDESC/Web browser./g' \
    -e 's/@@DEVELOPER_NAME/The Chromium Authors/g' \
    -e 's/@@PROJECT_LICENSE/BSD-3-Clause/g' \
    -e 's|@@PRODUCTURL|https://www.chromium.org/|g' \
    -e 's|@@BUGTRACKERURL|https://github.com/chimera-linux/cports/issues|g' \
    -e '/@@MAINTMAIL/d' \
    -e '/@@HELPURL/d' \
    -e '/@@appstream_screenshot_url/d' \
    chrome/installer/linux/common/appdata.xml.template \
    > chromium.appdata.xml
