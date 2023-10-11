import os


def invoke(pkg):
    badattrs = []

    for v in pkg.destdir.rglob("*"):
        xl = os.listxattr(v)

        # nothing to do
        if len(xl) == 0:
            continue

        attrs = pkg.file_xattrs.get(str(v.relative_to(pkg.destdir)), {})

        found_bad = False
        # go through attrs on the file and track undeclared ones
        for attr in xl:
            if attr not in attrs:
                found_bad = True
                break

        if not found_bad:
            continue

        badattrs.append(v)

    if len(badattrs) > 0:
        pkg.log_red("undeclared xattrs found for:")
        for f in badattrs:
            print(f"   {f}")
        pkg.error("cannot proceed")
