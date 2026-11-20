# Building and testing

## Plugin JARs

Use the Maven Wrapper and Java 25 for the current repositories. Older READMEs may still refer to the Gradle template.

```powershell
$env:JAVA_HOME = 'C:/PFAD/ZUM/JDK-25'
.\mvnw.cmd clean install
```

Install Core locally so dependent plugins can use its current classes. Then install the HcNpcs dependency and package Jobs.

```text
Core:   mvnw.cmd clean install
HcNpcs: mvnw.cmd clean install
Jobs:   mvnw.cmd clean package
```

Deploy artifacts from `target/`, such as `CorePlugin-1.0.0.jar`, `HcNpcs-1.0.0.jar`, and `JobsPlugin-1.0.0.jar`. Use the bundled Core JAR. `original-CorePlugin-1.0.0.jar` is the unbundled build output.

Use `clean` after removing or renaming classes so the JAR has no orphaned listener or debug classes. Maven's `0.7.7` dependency and the manifest's `^0.7.7` range follow separate version rules.

## Test coverage

The recorded NPC verification passed 54 Core, three HcNpcs, and six Jobs tests. Coverage includes transaction rollback, retries, concurrent balance and XP changes, and exact inventory plans.

Run MariaDB acceptance tests separately from the H2 suite. Check actual Hytale UI rendering and world instancing in a running client and server.

## Documentation

```text
python -m pip install -r requirements-docs.txt
python -m mkdocs build --strict
python -m mkdocs serve
```

The documentation workflow publishes public content and leaves private gameplay repositories untouched.
