pkgname = "qt6-qtdeclarative"
pkgver = "6.5.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DQT_BUILD_TESTS=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "perl",
    "python",
    "qt6-qtbase",
    "qt6-qtshadertools",
]
makedepends = ["qt6-qtbase-devel", "qt6-qtshadertools-devel"]
pkgdesc = "Qt6 declarative component"
license = (
    "LGPL-2.1-only AND LGPL-3.0-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0"
)
url = "https://www.qt.io"
source = f"https://download.qt.io/official_releases/qt/{pkgver[:-2]}/{pkgver}/submodules/qtdeclarative-everywhere-src-{pkgver}.tar.xz"
sha256 = "f7d631cd8ebc1491dad0f30f1b5326ae812bee4ad706e61157816a82bf588c97"
debug_level = 1  # defatten, especially with LTO
# FIXME
hardening = ["!int"]
# TODO
options = ["!cross"]


def do_check(self):
    # with offscreen    : 13% tests passed, 146 tests failed out of 167
    # +QML2_IMPORT_PATH : 78% tests passed,  37 tests failed out of 167
    excl_list = [
        "test_qml_app_deployment",  # missing /usr/lib/cmake/Qt6Quick/Qt6QuickConfig.cmake
        "module_includes",          # Could NOT find Qt6 (missing: Qt6_DIR)
        "cmake_tooling_imports",    # missing /usr/lib/cmake/Qt6Qml/Qt6QmlConfig.cmake
        "empty_qmldir",             # missing /usr/lib/cmake/Qt6Qml/Qt6QmlConfig.cmake
        "qmlquery",                 # missing /usr/lib/cmake/Qt6Qml/Qt6QmlConfig.cmake
        "qtquickcompiler",          # missing /usr/lib/cmake/Qt6Qml/Qt6QmlConfig.cmake
        "cmake_test_common_import_path",    # missing /usr/lib/cmake/Qt6Qml/Qt6QmlConfig.cmake
        "tst_qqmlapplicationengine",        # tst_qqmlapplicationengine::application(delayed quit) 'QString(testStdErr).endsWith(QString(expectedStdErr))' returned FALSE.
        "tst_qqmljsscope",          # missing builtins.qmltypes, jsroot.qmltypes
        "tst_qdebugmessageservice",         # Could not launch app  "/usr/lib/qt6/bin/qml"
        "tst_qqmldebugtranslationclient",   # Could not launch app  "/usr/lib/qt6/bin/qml"
        "tst_qqmldebugjs",          # Could not launch app  "/usr/lib/qt6/bin/qmlscene"
        "tst_qqmlinspector",        # Could not launch app  "/usr/lib/qt6/bin/qml"
        "tst_qqmlprofilerservice",  # Could not launch app  "/usr/lib/qt6/bin/qmlscene"
        "tst_qqmlenginedebuginspectorintegration",  # Could not launch app  "/usr/lib/qt6/bin/qml"
        "tst_qqmlenginecontrol",    # Could not launch app  "/usr/lib/qt6/bin/qmlscene"
        "tst_qqmldebuggingenabler",     # Could not launch app  "/usr/lib/qt6/bin/qmlscene"
        "tst_qqmldebugprocess",     # Timeout while waiting for QML debugging messages
        "tst_qqmlpreview",          # Could not launch app  "/usr/lib/qt6/bin/qml"
        "tst_qmlformat",            # qmlformat executable not found (looked for /usr/lib/qt6/bin/qmlformat)
        "tst_qmlimportscanner",     # qmlimportscanner executable not found (looked for /usr/lib/qt6/libexec/qmlimportscanner)
        "tst_qmllint",              # qmllint executable not found (looked for /usr/lib/qt6/bin/qmllint)
        "tst_qmltc_qprocess",       # qmltc executable not found (looked for /usr/lib/qt6/bin/qmltc)
        "tst_qmlplugindump",        # qmlplugindump executable not found (looked for /usr/lib/qt6/bin/qmlplugindump)
        "tst_qml",                  # tst_qml::initTestCase() 'QFileInfo(qmlPath).exists()' returned FALSE. ()
        "tst_qqmlextensionplugin",  # tst_qqmlextensionplugin::iidCheck() ASSERT failure in QTest::fetchData(): "Test data requested, but no testdata available"
        "text",                     # test failed
        "tst_qmldomitem",           # Error: Could not find builtins.qmltypes file
        "tst_dom_all",              # Error: Could not find builtins.qmltypes file
        "tst_basic",                # test failed
        "tst_fusion",               # test failed
        "tst_imagine",              # why ?
        "tst_material",             # why ?
        "tst_universal",            # why ?
        "tst_qquickiconimage",      # execution failed with exit code Segmentation fault
        "tst_qquickfiledialogimpl",     # why ?
        "tst_qquickfolderdialogimpl",   # test failed
    ]
    self.do(
        "ctest",
        "-E",
        "(" + "|".join(excl_list) + ")",
        wrksrc=self.make_dir,
        env={
            "QT_QPA_PLATFORM": "offscreen",
            "CTEST_OUTPUT_ON_FAILURE": "True",
            # qml stuff is not yet installed
            "QML2_IMPORT_PATH": str(
                self.chroot_cwd / f"{self.make_dir}/lib/qt6/qml"
            ),
        },
    )


def post_install(self):
    self.rm(self.destdir / "usr/tests", recursive=True)
    self.rm(self.destdir / "usr/lib/qt6/bin/testapp")
    for f in (self.destdir / "usr/lib/qt6/bin").glob("qqmldebug*"):
        f.unlink()


@subpackage("qt6-qtdeclarative-devel")
def _devel(self):
    self.depends += [
        f"qt6-qtshadertools-devel~{pkgver[:-2]}",
        f"qt6-qtbase-devel~{pkgver[:-2]}",
    ]

    return self.default_devel(
        extra=[
            "usr/lib/qt6/metatypes",
            "usr/lib/qt6/mkspecs",
            "usr/lib/qt6/modules",
            "usr/lib/qt6/plugins/qmltooling",
            "usr/lib/qt6/plugins/qmllint",
            "usr/lib/qt6/libexec/qmlcachegen",
            "usr/lib/qt6/libexec/qmlimportscanner",
            "usr/lib/qt6/libexec/qmltyperegistrar",
            "usr/lib/qt6/bin/qmlformat",
            "usr/lib/qt6/bin/qmllint",
            "usr/lib/qt6/bin/qmlpreview",
            "usr/lib/qt6/bin/qmlprofiler",
            "usr/lib/*.prl",
        ]
    )
