# sanitize style of service files


def _handle_svc(pkg, svcp):
    had_cl = False
    had_opt = False
    lintfail = False
    with svcp.open() as df:
        for ln in df:
            if ln.startswith("#"):
                continue
            ln = ln.strip()
            eq = ln.find("=")
            cl = ln.find(":")
            if cl > 0 and (eq < 0 or cl < eq):
                eq = -1
                key = ln[0:cl].strip()
                # val = ln[cl + 1 :].strip()
                had_cl = True
            elif eq > 0:
                if had_cl:
                    pkg.error(
                        f"service '{svcp.name}' has a '=' field after ':' field",
                        hint="dependency lines should be at the end of the service file",
                    )
                    lintfail = True
                cl = -1
                key = ln[0:eq].strip()
                # val = ln[eq + 1 :].strip()
            else:
                continue
            # ensure dep lines follow correct style
            match key:
                case (
                    "depends-on"
                    | "depends-ms"
                    | "waits-for"
                    | "depends-on.d"
                    | "depends-ms.d"
                    | "waits-for.d"
                    | "after"
                    | "before"
                ):
                    if eq > 0:
                        pkg.log_warn(
                            f"service '{svcp.name}' has a dependency field with '='",
                            # hint="dependencies should look like 'depends-on: foo', not 'depends-on = foo'",
                        )
                    if had_opt:
                        pkg.log_warn(
                            f"service '{svcp.name}' has a dependency field after options or load-options",
                            # hint="dependencies should be specified before options and load-options",
                        )
                case "options" | "load-options":
                    had_opt = True
                    if eq > 0:
                        pkg.log_warn(
                            f"service '{svcp.name}' has an options field '='",
                            # hint="options should look like 'options: foo', not 'options = foo'",
                        )
    if lintfail:
        pkg.error("service files have failed lint")


def invoke(pkg):
    pd = pkg.destdir / "usr/lib/dinit.d"

    for sd in [pd, pd / "user"]:
        if not sd.is_dir():
            continue
        for f in sd.iterdir():
            if f.is_file():
                _handle_svc(pkg, f)
