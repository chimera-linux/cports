pkgname = "tesseract"
pkgver = "5.5.2"
pkgrel = 0
build_style = "gnu_configure"
# also install training tools
make_build_args = ["training"]
make_install_args = ["training-install"]
hostmakedepends = [
    "asciidoc",
    "automake",
    "libxslt-progs",
    "pkgconf",
    "slibtool",
]
makedepends = [
    "curl-devel",
    "icu-devel",
    "leptonica-devel",
    "libarchive-devel",
    "pango-devel",
]
depends = [
    "tesseract-data-eng",
    "tesseract-data-osd",
]
renames = ["tesseract-libs"]
pkgdesc = "OCR engine"
license = "Apache-2.0"
url = "https://tesseract-ocr.github.io"
source = f"https://github.com/tesseract-ocr/tesseract/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "6235ea0dae45ea137f59c09320406f5888383741924d98855bd2ce0d16b54f21"
# check: tests require external data
options = ["!check"]


@subpackage("tesseract-training")
def _(self):
    self.subdesc = "training tools"

    return [
        "cmd:ambiguous_words",
        "cmd:classifier_tester",
        "cmd:cntraining",
        "cmd:combine_lang_model",
        "cmd:combine_tessdata",
        "cmd:dawg2wordlist",
        "cmd:lstmeval",
        "cmd:lstmtraining",
        "cmd:merge_unicharsets",
        "cmd:mftraining",
        "cmd:set_unicharset_properties",
        "cmd:shapeclustering",
        "cmd:text2image",
        "cmd:unicharset_extractor",
        "cmd:wordlist2dawg",
    ]


@subpackage("tesseract-devel")
def _(self):
    return self.default_devel()
