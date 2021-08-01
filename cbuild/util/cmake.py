from cbuild.core import paths

def configure(
    pkg, cmake_dir = None, build_dir = "build", extra_args = [],
    cross_build = None
):
    if cmake_dir:
        cdir = pkg.chroot_cwd / cmake_dir
    else:
        cdir = pkg.chroot_cwd

    (pkg.cwd / build_dir).mkdir(parents = True, exist_ok = True)

    cargs = []

    if pkg.bootstrapping:
        with open(
            pkg.cwd / build_dir / "bootstrap.cmake", "w"
        ) as infile:
            infile.write(f"""
SET(CMAKE_SYSTEM_NAME Linux)
SET(CMAKE_SYSTEM_VERSION 1)

SET(CMAKE_C_COMPILER   {pkg.get_tool("CC")})
SET(CMAKE_CXX_COMPILER {pkg.get_tool("CXX")})

SET(CMAKE_FIND_ROOT_PATH  "{paths.masterdir() / 'usr'};{paths.masterdir()}")

SET(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
SET(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)
""")
        cargs.append("-DCMAKE_TOOLCHAIN_FILE=bootstrap.cmake")
    elif pkg.build_profile.cross and cross_build != False:
        # map known profiles to cmake arch
        cmake_cpu = {
            "aarch64": "aarch64",
            "ppc64le": "ppc64le",
            "ppc64": "ppc64",
            "x86_64": "x86_64",
            "riscv64": "riscv64"
        }.get(pkg.build_profile.arch, None)

        if not cmake_cpu:
            pkg.error(f"unknown architecture: {pkg.build_profile.arch}")

        sroot = pkg.build_profile.sysroot

        with open(
            pkg.cwd / build_dir / "cross.cmake", "w"
        ) as infile:
            infile.write(f"""
SET(CMAKE_SYSTEM_NAME Linux)
SET(CMAKE_SYSTEM_VERSION 1)

SET(CMAKE_C_COMPILER   {pkg.get_tool("CC")})
SET(CMAKE_CXX_COMPILER {pkg.get_tool("CXX")})
SET(CMAKE_C_COMPILER_TARGET {pkg.build_profile.short_triplet})
SET(CMAKE_CXX_COMPILER_TARGET {pkg.build_profile.short_triplet})
SET(CMAKE_ASM_COMPILER_TARGET {pkg.build_profile.short_triplet})
SET(CMAKE_CROSSCOMPILING TRUE)
SET(CMAKE_SYSROOT "{sroot}")

SET(CMAKE_SYSTEM_PROCESSOR {cmake_cpu})

SET(CMAKE_FIND_ROOT_PATH  "{sroot / 'usr'};{sroot}")

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
        wrksrc = build_dir, env = {
            "CMAKE_GENERATOR": (
                "Ninja" if pkg.make_cmd == "ninja" else "Unix Makefiles"
            )
        }
    )
