# keep pkgver AND pkgrel in sync with qt6-qtwayland
pkgname = "qt6-qtbase"
pkgver = "6.6.1"
pkgrel = 2
build_style = "cmake"
configure_args = [
    "-DINSTALL_DATADIR=share/qt6",
    "-DINSTALL_ARCHDATADIR=lib/qt6",
    "-DINSTALL_BINDIR=lib/qt6/bin",
    "-DINSTALL_PUBLICBINDIR=usr/bin",
    "-DINSTALL_DOCDIR=share/doc/qt6",
    "-DINSTALL_MKSPECSDIR=lib/qt6/mkspecs",
    "-DINSTALL_INCLUDEDIR=include/qt6",
    "-DINSTALL_EXAMPLESDIR=lib/qt6/examples",
    "-DINSTALL_TESTSDIR=lib/qt6/tests",
    "-DINSTALL_SYSCONFDIR=/etc/xdg",
    "-DQT_FEATURE_journald=OFF",
    "-DQT_FEATURE_reduce_relocations=OFF",
    "-DQT_FEATURE_openssl_linked=ON",
    "-DQT_FEATURE_system_xcb_xinput=ON",
    "-DQT_FEATURE_system_sqlite=ON",
    "-DQT_FEATURE_libproxy=ON",
    "-DQT_FEATURE_syslog=ON",
    "-DQT_FEATURE_vulkan=ON",
    "-DQT_FEATURE_qmake=ON",
    "-DQT_FEATURE_xcb=ON",
    "-DBUILD_WITH_PCH=OFF",
    "-DQT_BUILD_TESTS=ON",
]
hostmakedepends = ["cmake", "ninja", "perl", "pkgconf", "xmlstarlet"]
makedepends = [
    "zlib-devel",
    "zstd-devel",
    "dbus-devel",
    "double-conversion-devel",
    "libxcb-devel",
    "xcb-util-image-devel",
    "xcb-util-keysyms-devel",
    "xcb-util-renderutil-devel",
    "xcb-util-wm-devel",
    "xcb-util-cursor-devel",
    "mesa-devel",
    "glib-devel",
    "pcre2-devel",
    "icu-devel",
    "mtdev-devel",
    "harfbuzz-devel",
    "libpng-devel",
    "tslib-devel",
    "libinput-devel",
    "gtk+3-devel",
    "cups-devel",
    "libproxy-devel",
    "brotli-devel",
    "sqlite-devel",
    "heimdal-devel",
    "libb2-devel",
    "libxkbcommon-devel",
    "wayland-devel",
    "linux-headers",
    "vulkan-headers",
    "vulkan-loader-devel",
]
depends = ["shared-mime-info"]
pkgdesc = "Qt application framework (6.x)"
maintainer = "q66 <q66@chimera-linux.org>"
license = (
    "LGPL-2.1-only AND LGPL-3.0-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0"
)
url = "https://www.qt.io"
source = f"https://download.qt.io/official_releases/qt/{pkgver[:-2]}/{pkgver}/submodules/qtbase-everywhere-src-{pkgver}.tar.xz"
sha256 = "450c5b4677b2fe40ed07954d7f0f40690068e80a94c9df86c2c905ccd59d02f7"
debug_level = 1  # defatten, especially with LTO
# FIXME
hardening = ["!int"]
# TODO
options = ["!cross"]

if self.profile().arch == "aarch64":
    configure_args += ["-DQT_FEATURE_opengles2=ON"]

if self.profile().cross:
    hostmakedepends += ["qt6-qtbase"]
    configure_args += ["-DQT_FORCE_BUILD_TOOLS=ON"]


def init_configure(self):
    if self.has_lto():
        self.configure_args += ["-DCMAKE_INTERPROCEDURAL_OPTIMIZATION=ON"]


def init_check(self):
    excl_list = [
        "tst_selftests",  # requires valgrind
        "tst_qmake",  # Could not find qmake spec 'linux-clang'.
        "tst_moc",  # tst_Moc::initTestCase() 'fi.exists()' returned FALSE. ()
        "tst_rcc",  # Could not start "/builddir/qt6-base-6.5.1/build/lib/qt6/libexec/rcc": chdir: No such file or directory
        "tst_qstandardpaths",  # using / as runtime directory ? wrong permission then
        "tst_qresourceengine",  # tst_QResourceEngine::lastModified() '!fi.lastModified().isValid()' returned FALSE.
        "tst_qfilesystemwatcher",  # tst_QFileSystemWatcher::addPaths() Compared lists have different sizes.
        "tst_qpluginloader",  # tst_QPluginLoader::loadDebugObj() 'QFile::exists(QFINDTESTDATA("elftest/debugobj.so"))' returned FALSE. ()
        "tst_qlibrary",  # tst_QLibrary::initTestCase() 'QDir::setCurrent(testdatadir)' returned FALSE. (Could not chdir to )
        "tst_qtextstream",  # tst_QTextStream::initTestCase() '!m_rfc3261FilePath.isEmpty()' returned FALSE. ()
        "test_build_simple_widget_app_qmake",  # fatal error: 'QApplication' file not found
        "test_interface",  # requires Qt6WidgetsConfig.cmake (present in build/lib/cmake/Qt6Widgets/Qt6WidgetsConfig.cmake)
        "test_add_big_resource",  # No data signature found
        "mockplugins",  # Unknown platform linux-clang
        "test_plugin_flavor_static",  # test fails to configure
        "test_plugin_flavor_shared",  # flaky
        "test_import_plugins",  # not run: dep of mockplugins
        "test_add_resources_big_resources",  # No data signature found
        "tst_qaddpreroutine",  # Unknown platform linux-clang
        "test_static_resources",  # Unknown platform linux-clang
        "test_generating_cpp_exports",  # Unknown platform linux-clang
        "test_widgets_app_deployment",  # Subprocess aborted
        "tst_qcolorspace",  # tst_QColorSpace::imageConversion64PM(sRGB -> Adobe RGB) Compared values are not the same
        "tst_qdebug",  # tst_QDebug::qDebugQFlags() Compared values are not the same
        "tst_qdialogbuttonbox",  # tst_QDialogButtonBox::standardButtons() Compared values are not the same
        "tst_qopenglwindow",  # execution failed with exit code Segmentation fault.
        "tst_qimagereader",  # execution failed with exit code Segmentation fault.
        "tst_qicoimageformat",  # execution failed with exit code Segmentation fault.
        "tst_qimage",  # execution failed with exit code Segmentation fault.
        "tst_qpainter",  # execution failed with exit code Segmentation fault.
        "tst_qfont",  # tst_QFont::defaultFamily(serif) 'QFontDatabase::hasFamily(familyForHint)' returned FALSE.
        "tst_qfontdatabase",  # tst_QFontDatabase::systemFixedFont() 'fdbSaysFixed' returned FALSE.
        "tst_qfontmetrics",  # tst_QFontMetrics::zeroWidthMetrics() Compared values are not the same
        "tst_qglyphrun",  # tst_QGlyphRun::mixedScripts() Compared values are not the same
        "tst_qrawfont",  # tst_QRawFont::unsupportedWritingSystem(Default hinting preference) 'layoutFont.familyName() != QString::fromLatin1("QtBidiTestFont")' returned FALSE
        "tst_qtextcursor",  # tst_QTextCursor::insertHtml(insert as text in new block at end of heading) Compared values are not the same
        "tst_qtextdocumentlayout",  # tst_QTextDocumentLayout::imageAtRightAlignedTab() Compared doubles are not the same (fuzzy compare)
        "tst_qtextmarkdownimporter",  # tst_QTextMarkdownImporter::lists(styled spans in list items) Compared values are not the same
        "tst_qopenglconfig",  # tst_QOpenGlConfig::testGlConfiguration() 'context.create()' returned FALSE
        "tst_qopengl",  # tst_QOpenGL::sharedResourceCleanup(Using QWindow) 'ctx->create()' returned FALSE
        "tst_qx11info",  # tst_QX11Info::startupId() Compared values are not the same
        "tst_qdnslookup",  # Resolver functions not found (voidlinux: Some glibc specific DNS Lookup)
        "tst_qfiledialog",  # tst_QFiledialog::historyBack() Compared values are not the same
        "tst_qgraphicsproxywidget",  # tst_QGraphicsProxyWidget::focusOutEvent(widget, focus to other widget) Widget should have focus but doesn't
        "tst_qgraphicsview",  # execution failed with exit code Segmentation fault.
        "tst_qapplication",  # tst_QApplication::libraryPaths() '!testDir.isEmpty()' returned FALSE. ()
        "tst_qfontcombobox",  # tst_QFontComboBox::currentFontChanged() Compared values are not the same
        "tst_qlineedit",  # tst_QLineEdit::setInputMask(keys blank=input) To eat blanks or not? Known issue. Task 43172
        "tst_qmenubar",  # tst_QLineEdit::returnPressed_maskvalidator(mask '999', intfix validator(0,999), input '12<cr>') QIntValidator has changed behaviour. Does not accept spaces.
        "tst_qmetaobject",  # tst_QMetaObject::enumDebugStream(verbosity=3) Not all expected messages were received
        "tst_qmetaobject_compat",  # tst_QMetaObject_CompatQArg::enumDebugStream(verbosity=2) Not all expected messages were received
        "tst_qopenglwidget",  # execution failed with exit code Segmentation fault.
        "tst_qcomplextext",  # tst_QComplexText::bidiCursorMovement(data46) 'newX <= x' returned FALSE
        "tst_qsharedmemory",  # tst_QSharedMemory::simpleThreadedProducerConsumer(POSIX:5 consumers, producer is this) 'p.producer.isAttached()' returned FALSE
    ]
    self.make_check_args += ["-E", "(" + "|".join(excl_list) + ")"]
    self.make_check_env["QT_QPA_PLATFORM"] = "offscreen"
    self.make_check_env["QMAKESPEC"] = f"{self.chroot_cwd}/mkspecs/linux-clang"


def post_install(self):
    # remove installed checks files (because of "-DQT_BUILD_TESTS=ON")
    self.rm(self.destdir / "usr/tests", recursive=True)
    self.rm(self.destdir / "usr/lib/qt6/tests", recursive=True)
    self.rm(self.destdir / "usr/lib/qt6/bin/tst_qhashseed_helper")
    self.rm(self.destdir / "usr/lib/qt6/bin/testSetWorkingDirectory")
    self.rm(self.destdir / "usr/lib/qt6/bin/testGuiProcess")
    self.rm(self.destdir / "usr/lib/qt6/bin/testForwarding")
    self.rm(self.destdir / "usr/lib/qt6/bin/testDetached")
    self.rm(self.destdir / "usr/lib/qt6/bin/syslocaleapp")
    self.rm(self.destdir / "usr/lib/qt6/bin/socketprocess")
    self.rm(self.destdir / "usr/lib/qt6/bin/qfileopeneventexternal")
    self.rm(self.destdir / "usr/lib/qt6/bin/qcommandlineparser_test_helper")
    self.rm(self.destdir / "usr/lib/qt6/bin/paster")
    self.rm(self.destdir / "usr/lib/qt6/bin/modal_helper")
    self.rm(self.destdir / "usr/lib/qt6/bin/fileWriterProcess")
    self.rm(self.destdir / "usr/lib/qt6/bin/echo")
    self.rm(self.destdir / "usr/lib/qt6/bin/desktopsettingsaware_helper")
    self.rm(self.destdir / "usr/lib/qt6/bin/crashingServer")
    self.rm(self.destdir / "usr/lib/qt6/bin/copier")
    self.rm(self.destdir / "usr/lib/qt6/bin/clientserver")
    self.rm(self.destdir / "usr/lib/qt6/bin/nospace")
    self.rm(self.destdir / "usr/lib/qt6/bin/one space")
    self.rm(self.destdir / "usr/lib/qt6/bin/two space s")
    self.install_file(self.files_path / "target_qt.conf", "usr/lib/qt6/bin")
    # eliminate hardlinks
    for f in (self.destdir / "usr/lib/qt6/bin").glob("*6"):
        nsname = f.name.removesuffix("6")
        f.with_name(nsname).unlink()
        self.install_link(f.name, f"usr/lib/qt6/bin/{nsname}")

    # link publicbindir utils to usr/bin, like qmake6
    # used outside of cmake
    self.install_dir("usr/bin")
    with open(
        self.cwd / self.make_dir / "user_facing_tool_links.txt", "r"
    ) as f:
        for line in f.readlines():
            self.install_link(*line.split())


@subpackage("qt6-qtbase-gui")
def _gui(self):
    self.depends += ["hicolor-icon-theme"]
    self.pkgdesc = f"{pkgdesc} (GUI)"

    return [
        "usr/lib/libQt6Gui.so.*",
        "usr/lib/libQt6XcbQpa.so.*",
        "usr/lib/libQt6EglFSDeviceIntegration.so.*",
        "usr/lib/libQt6EglFsKmsGbmSupport.so.*",
        "usr/lib/libQt6EglFsKmsSupport.so.*",
        "usr/lib/libQt6OpenGL.so.*",
        "usr/lib/qt6/plugins/generic",
        "usr/lib/qt6/plugins/platforms",
        "usr/lib/qt6/plugins/xcbglintegrations",
        "usr/lib/qt6/plugins/imageformats",
        "usr/lib/qt6/plugins/egldeviceintegrations",
        "usr/lib/qt6/plugins/platforminputcontexts",
        "usr/lib/qt6/plugins/platformthemes",
    ]


def _libpkg(name, libname, desc, extra=[]):
    @subpackage(f"qt6-qtbase-{name}")
    def _sp(self):
        self.pkgdesc = f"{pkgdesc} ({desc})"
        return [f"usr/lib/libQt6{libname}.so.*"] + extra


for _sp in [
    ("opengl-widgets", "OpenGLWidgets", "OpenGL widgets"),
    ("dbus", "DBus", "DBus"),
    ("core", "Core", "Core"),
    (
        "printsupport",
        "PrintSupport",
        "Print support",
        ["usr/lib/qt6/plugins/printsupport"],
    ),
    ("concurrent", "Concurrent", "Concurrency"),
    ("widgets", "Widgets", "Widgets"),
    (
        "network",
        "Network",
        "Network",
        [
            "usr/lib/qt6/plugins/networkinformation",
            "usr/lib/qt6/plugins/tls",
        ],
    ),
    (
        "sql",
        "Sql",
        "SQL",
        [
            "usr/lib/qt6/plugins/sqldrivers",
        ],
    ),
    ("test", "Test", "Test"),
    ("xml", "Xml", "XML"),
]:
    _libpkg(*_sp)


@subpackage("qt6-qtbase-devel")
def _devel(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"] + makedepends
    return self.default_devel(
        extra=[
            "usr/bin/androiddeployqt6",
            "usr/bin/qmake6",
            "usr/lib/qt6/metatypes",
            "usr/lib/qt6/mkspecs",
            "usr/lib/qt6/modules",
            "usr/lib/*.prl",
        ]
    )
