import sys
import atexit
import os


def restart():
    if "SHAXSIY_DO_NOT_RESTART" in os.environ:
        print("Loopga tushib qoldim, chiqish")
        sys.exit(0)

    print("🔄 Restarting...")

    atexit.register(
        lambda: os.execl(
            sys.executable,
            sys.executable,
            "-m",
            os.path.relpath(
                os.path.abspath(
                    os.path.dirname(
                        os.path.abspath(__file__),
                    ),
                ),
            ),
            *(sys.argv[1:]),
        )
    )

    os.environ["SHAXSIY_DO_NOT_RESTART"] = "1"

    sys.exit(0)
