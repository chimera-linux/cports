import stat


def invoke(pkg):
    badbins = []

    for v in pkg.destdir.rglob("*"):
        st = v.lstat()
        sm = st.st_mode

        # must be a regular file
        if not stat.S_ISREG(sm):
            continue

        # if not suid or setgid, skip
        if not ((sm & stat.S_ISUID) or (sm & stat.S_ISGID)):
            continue

        vr = v.relative_to(pkg.destdir)
        found_suid = True

        for f in pkg.file_modes:
            if vr.match(f):
                break
        else:
            found_suid = False

        # if matching whitelist, it's okay
        if found_suid:
            continue

        badbins.append(v)

    if len(badbins) > 0:
        pkg.log_red("forbidden setuid/setgid files:")
        for f in badbins:
            print(f"  {f}")
        pkg.error("cannot proceed")
