from cbuild.core import paths
from cbuild import cpu

def configure(pkg, cmake_dir = None, build_dir = "build", extra_args = []):
    if cmake_dir:
        cdir = str(pkg.chroot_wrksrc / cmake_dir)
    else:
        cdir = str(pkg.chroot_wrksrc)

    (pkg.abs_build_wrksrc / build_dir).mkdir(parents = True, exist_ok = True)

    mdir = str(paths.masterdir())
    cargs = []

    if pkg.bootstrapping:
        with open(
            pkg.abs_build_wrksrc / build_dir / "bootstrap.cmake", "w"
        ) as infile:
            infile.write(f"""
SET(CMAKE_SYSTEM_NAME Linux)
SET(CMAKE_SYSTEM_VERSION 1)

SET(CMAKE_C_COMPILER   {pkg.tools["CC"]})
SET(CMAKE_CXX_COMPILER {pkg.tools["CXX"]})

SET(CMAKE_FIND_ROOT_PATH  "{mdir}/usr;{mdir}")

SET(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
SET(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)
""")
        cargs.append("-DCMAKE_TOOLCHAIN_FILE=bootstrap.cmake")
    elif pkg.build_profile.cross:
        cmake_cpu = cpu.match_arch(pkg.build_profile.arch,
            "arm*",     "arm",
            "aarch64*", "aarch64",
            "ppc64le*", "ppc64le",
            "ppc64*",   "ppc64",
            "ppc*",     "ppc",
            "x86_64*",  "x86_64",
            "i686*",    "x86",
            "riscv64*", "riscv64",
            "*", None
        )

        sroot = str(pkg.build_profile.sysroot)

        with open(
            pkg.abs_build_wrksrc / build_dir / "cross.cmake", "w"
        ) as infile:
            infile.write(f"""
SET(CMAKE_SYSTEM_NAME Linux)
SET(CMAKE_SYSTEM_VERSION 1)

SET(CMAKE_C_COMPILER   {pkg.tools["CC"]})
SET(CMAKE_CXX_COMPILER {pkg.tools["CXX"]})
SET(CMAKE_C_COMPILER_TARGET {pkg.build_profile.short_triplet})
SET(CMAKE_CXX_COMPILER_TARGET {pkg.build_profile.short_triplet})
SET(CMAKE_ASM_COMPILER_TARGET {pkg.build_profile.short_triplet})
SET(CMAKE_CROSSCOMPILING TRUE)
SET(CMAKE_SYSROOT "{sroot}")

SET(CMAKE_SYSTEM_PROCESSOR {cmake_cpu})

SET(CMAKE_FIND_ROOT_PATH  "{sroot}/usr;{sroot}")

SET(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)
SET(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
SET(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)
""")
        cargs.append("-DCMAKE_TOOLCHAIN_FILE=cross.cmake")

    pkg.do(
        "cmake", cargs + [
            "-DCMAKE_INSTALL_PREFIX=/usr",
            "-DCMAKE_BUILD_TYPE=None",
            "-DCMAKE_INSTALL_LIBDIR=lib",
            "-DCMAKE_INSTALL_SBINDIR=bin"
        ] + pkg.configure_args + extra_args + [cdir],
        wrksrc = build_dir, build = True, env = {
            "CMAKE_GENERATOR": (
                "Ninja" if pkg.make_cmd == "ninja" else "Unix Makefiles"
            )
        }
    )
