// Root build.sbt for Scala Steward compatibility
// This aggregates all Akka sample subprojects

ThisBuild / scalaVersion := "2.13.12"

// Aggregate all sample projects
lazy val root = (project in file("."))
  .aggregate(
    // Scala projects with build.sbt
    `akka-sample-cluster-client-grpc-scala`,
    `akka-sample-cluster-scala`,
    `akka-sample-cluster-java`,
    `akka-sample-distributed-data-scala`,
    `akka-sample-distributed-data-java`,
    `akka-sample-distributed-workers-scala`,
    `akka-sample-fsm-scala`,
    `akka-sample-kafka-to-sharding-scala`,
    `akka-sample-persistence-dc-scala`,
    `akka-sample-persistence-scala`,
    `akka-sample-sharding-scala`,
    `akka-sample-sharding-java`
  )
  .settings(
    name := "akka-samples-root",
    // Don't publish root project
    publish / skip := true
  )

// Define subprojects
lazy val `akka-sample-cluster-client-grpc-scala` = project in file("akka-sample-cluster-client-grpc-scala")
lazy val `akka-sample-cluster-scala` = project in file("akka-sample-cluster-scala")
lazy val `akka-sample-cluster-java` = project in file("akka-sample-cluster-java")
lazy val `akka-sample-distributed-data-scala` = project in file("akka-sample-distributed-data-scala")
lazy val `akka-sample-distributed-data-java` = project in file("akka-sample-distributed-data-java")
lazy val `akka-sample-distributed-workers-scala` = project in file("akka-sample-distributed-workers-scala")
lazy val `akka-sample-fsm-scala` = project in file("akka-sample-fsm-scala")
lazy val `akka-sample-kafka-to-sharding-scala` = project in file("akka-sample-kafka-to-sharding-scala")
lazy val `akka-sample-persistence-dc-scala` = project in file("akka-sample-persistence-dc-scala")
lazy val `akka-sample-persistence-scala` = project in file("akka-sample-persistence-scala")
lazy val `akka-sample-sharding-scala` = project in file("akka-sample-sharding-scala")
lazy val `akka-sample-sharding-java` = project in file("akka-sample-sharding-java")

// =============================================================================
// SECURITY FIX: Override vulnerable transitive dependencies
// Fixes 7 Dependabot security alerts
// Date: November 6, 2025
// =============================================================================
ThisBuild / dependencyOverrides ++= Seq(
  // Logback - CVE-2021-42550 (HIGH severity)
  "ch.qos.logback" % "logback-classic" % "1.2.11",
  "ch.qos.logback" % "logback-core" % "1.2.11",
  
  // Jackson - Multiple CVEs (HIGH severity)
  "com.fasterxml.jackson.core" % "jackson-databind" % "2.13.5",
  "com.fasterxml.jackson.core" % "jackson-core" % "2.13.5",
  "com.fasterxml.jackson.core" % "jackson-annotations" % "2.13.5",
  "com.fasterxml.jackson.module" %% "jackson-module-scala" % "2.13.5",
  
  // Akka - Ensure secure versions
  "com.typesafe.akka" %% "akka-actor" % "2.6.20",
  "com.typesafe.akka" %% "akka-stream" % "2.6.20",
  "com.typesafe.akka" %% "akka-cluster" % "2.6.20",
  "com.typesafe.akka" %% "akka-actor-typed" % "2.6.20",
  "com.typesafe.akka" %% "akka-persistence" % "2.6.20"
)

