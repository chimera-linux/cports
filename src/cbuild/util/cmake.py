from cbuild.core import paths


def configure(
    pkg, cmake_dir=None, build_dir=None, extra_args=[], env={}, cross_build=None
):
    if cmake_dir:
        cdir = pkg.chroot_cwd / cmake_dir
    else:
        cdir = pkg.chroot_cwd

    if not build_dir:
        build_dir = pkg.make_dir

    (pkg.cwd / build_dir).mkdir(parents=True, exist_ok=True)

    cargs = []

    if pkg.stage == 0:
        with open(pkg.cwd / build_dir / "bootstrap.cmake", "w") as infile:
            infile.write(
                f"""
SET(CMAKE_SYSTEM_NAME Linux)
SET(CMAKE_SYSTEM_VERSION 1)

SET(CMAKE_C_COMPILER   {pkg.get_tool("CC")})
SET(CMAKE_CXX_COMPILER {pkg.get_tool("CXX")})

SET(CMAKE_FIND_ROOT_PATH  "{paths.bldroot() / 'usr'};{paths.bldroot()}")

SET(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
SET(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)
"""
            )
        cargs.append("-DCMAKE_TOOLCHAIN_FILE=bootstrap.cmake")
    elif pkg.profile().cross and cross_build is not False:
        # map known profiles to cmake arch
        match pkg.profile().arch:
            case "aarch64" | "ppc64le" | "ppc64" | "x86_64" | "riscv64":
                cmake_cpu = pkg.profile().arch
            case _:
                pkg.error(f"unknown architecture: {pkg.profile().arch}")

        sroot = pkg.profile().sysroot

        with open(pkg.cwd / build_dir / "cross.cmake", "w") as infile:
            infile.write(
                f"""
SET(CMAKE_SYSTEM_NAME Linux)
SET(CMAKE_SYSTEM_VERSION 1)

SET(CMAKE_C_COMPILER   {pkg.get_tool("CC")})
SET(CMAKE_CXX_COMPILER {pkg.get_tool("CXX")})
SET(CMAKE_C_COMPILER_TARGET {pkg.profile().triplet})
SET(CMAKE_CXX_COMPILER_TARGET {pkg.profile().triplet})
SET(CMAKE_ASM_COMPILER_TARGET {pkg.profile().triplet})
SET(CMAKE_CROSSCOMPILING TRUE)
SET(CMAKE_SYSROOT "{sroot}")

SET(CMAKE_SYSTEM_PROCESSOR {cmake_cpu})

SET(CMAKE_FIND_ROOT_PATH  "{sroot / 'usr'};{sroot}")

SET(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)
SET(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
SET(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)
"""
            )
        cargs.append("-DCMAKE_TOOLCHAIN_FILE=cross.cmake")

    eenv = {
        "CMAKE_GENERATOR": (
            "Ninja" if pkg.make_cmd == "ninja" else "Unix Makefiles"
        )
    }

    eenv.update(pkg.configure_env)
    eenv.update(env)

    # this is necessary for lto to work correctly
    if pkg.stage >= 2:
        cargs += [
            f"-DCMAKE_AR=/usr/bin/{pkg.get_tool('AR')}",
            f"-DCMAKE_NM=/usr/bin/{pkg.get_tool('NM')}",
            f"-DCMAKE_RANLIB=/usr/bin/{pkg.get_tool('RANLIB')}",
        ]

    pkg.do(
        "cmake",
        *cargs,
        "-DCMAKE_INSTALL_PREFIX=/usr",
        "-DCMAKE_BUILD_TYPE=None",
        "-DCMAKE_INSTALL_LIBDIR=lib",
        "-DCMAKE_INSTALL_SBINDIR=bin",
        *pkg.configure_args,
        *extra_args,
        cdir,
        wrksrc=build_dir,
        env=eenv,
    )
