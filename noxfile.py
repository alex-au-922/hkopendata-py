import nox
import tempfile


@nox.session(python=["3.8", "3.9", "3.10", "3.11", "3.12", "3.13"])
def test(session: nox.Session):
    session.install("poetry")
    with tempfile.TemporaryDirectory() as tmpdir:
        with tempfile.NamedTemporaryFile("+w", dir=tmpdir, delete=False) as f:
            session.run(
                "poetry",
                "export",
                "--format=requirements.txt",
                f"--output={f.name}",
                "--with",
                "dev",
                "--without-hashes",
                external=True,
            )
        session.install(f"-r{f.name}")
        session.run("pytest", *session.posargs)
