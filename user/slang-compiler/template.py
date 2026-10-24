pkgname = "slang-compiler"
pkgver = "2026.20"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DSLANG_ENABLE_DXIL=FALSE",
    "-DSLANG_SLANG_LLVM_FLAVOR=USE_SYSTEM_LLVM",
    "-DSLANG_INSTALL_USER_SKILLS=OFF",
    "-DSLANG_RHI_ENABLE_OPTIX=OFF",
]
hostmakedepends = [
    "clang-devel",
    "cmake",
    "glib-devel-static",
    "llvm-devel",
    "ninja",
    "pkgconf",
    "python",
    "zlib-ng-compat-devel",
]
pkgdesc = "Compiler for the slang-shader language"
license = "Apache-2.0 WITH LLVM-exception"
url = "https://shader-slang.org"
source = [
    f"https://github.com/shader-slang/slang/archive/refs/tags/v{pkgver}.tar.gz",
    # This is sooooooo arghhhhh: manually vendor all the required submodules from github
    #
    # Updating the template just consists of updating the pinned revisions using the
    # information found in .gitmodules
    "https://github.com/martinus/unordered_dense/archive/73f3cbb237e84d483afafc743f1f14ec53e12314.tar.gz",
    "https://github.com/richgel999/miniz/archive/6ef6c68f4fcbb8287aa8edf9c6670804932f41c6.tar.gz",
    "https://github.com/nlohmann/json/archive/d96329f8d6dee5da67c5ebd861acab25445d0ddb.tar.gz",
    "https://github.com/swiftlang/swift-cmark/archive/924936d0427cb25a61169739a7660230bffa6ea6.tar.gz",
    "https://github.com/KhronosGroup/Vulkan-Headers/archive/387259ecf4b0fe0cfac161b1d0b0a74e42796710.tar.gz",
    "https://github.com/lz4/lz4/archive/7f71be01f2c6f6b2c3cddb67eef8c38eab12ffd4.tar.gz",
    "https://github.com/KhronosGroup/SPIRV-Headers/archive/cb42dec3830d3ac67fa449ecdc0c0f73d5e74498.tar.gz",
    "https://github.com/KhronosGroup/SPIRV-Tools/archive/7a88476ddf5f541ba553cbe009227d7510d258eb.tar.gz",
    "https://github.com/KhronosGroup/glslang/archive/d1f52c8993a501bd52d4fbd044bfeb9ecdceb9f4.tar.gz",
    "https://github.com/shader-slang/slang-rhi/archive/b856e6350ea09f63a16a6c7497faa1d741fdd735.tar.gz",
    "https://github.com/fastfloat/fast_float/archive/e0b53eaf63c6d00e0725788ef1dbb759aa321d79.tar.gz",
    "https://github.com/lua/lua/archive/3fe7be956f23385aa1950dc31e2f25127ccfc0ea.tar.gz",
    "https://github.com/g-truc/glm/archive/efec5db081e3aad807d0731e172ac597f6a39447.tar.gz",
    "https://github.com/tinyobjloader/tinyobjloader/archive/d541711a794343de4ef5ea76f037c9fb9c127a55.tar.gz",
    "https://github.com/ocornut/imgui/archive/8936b58fe26e8c3da834b8f60b06511d537b4c63.tar.gz",
]
source_paths = [
    ".",
    "external/unordered_dense",
    "external/miniz",
    "external/nlohmann-json",
    "external/cmark",
    "external/vulkan",
    "external/lz4",
    "external/spirv-headers",
    "external/spirv-tools",
    "external/glslang",
    "external/slang-rhi",
    "external/fast_float",
    "external/lua",
    "external/glm",
    "external/tinyobjloader",
    "external/imgui",
]
sha256 = [
    "f58bda28ae5ad57e098b1b028d03b0ef466bb70b7d4f9fe266722938ec6453cb",
    "16188ed4804a670f6b00637a53e135190668dddc12b10f5233e20b403b9df9e2",
    "d9ef3c09f98b0dba3aa60e520284ed54042b0baa86116312be3f36e26393ae27",
    "07160d1e48a728dea19c56ef061a7214ec1043c3436848ebbde462c44fbf487c",
    "1c51659bd47c34df1c8976f893adc43ba039a98f6eac4fa95d53d1e08ba6072a",
    "d90e6eb2ed69efce8cf49793404b09fbdb7066ea2b624f3f3ea3c8dbc5fa52a0",
    "199498e55cbc1f48cd60617c4e5e911da69759bb3e60f7ff8563b31bcf00db05",
    "117010e525fe36b1ce006e0e58a6e0a3b415aabc9179d912b92737f41f3f994f",
    "5be2b9dc644341f2717d34f095972c6fb934377379b8edb24c939f89d04249e6",
    "d914157124abcec9e7d3bd8ba99f023d4cada87e67f38a3b76e4b70c15fd2c07",
    "4c629dc48692fadfdb9dccaa035b18bf85573a1462094823f0078d7577f64c71",
    "f6259a3543e75ae705ec80835d1568622b444d389922dcc314af7250c26e8643",
    "4776526f89abeea61cce41a056577859180dbb2d4cb6c1dad00955872a1007bb",
    "15cd88d9a099c0e944efa775032979509394574e11ff98f437500cb3f103845a",
    "95d14866c083640365245a3241b421c0bbad5c9d7c816bb2cbd61a00ff4d40be",
    "a1e4443190d78976e0901039dd2207e1d59a4b5b818489232568bdb69ff79ce6",
]
hardening = []
options = ["!cross"]
