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


// Security: Override vulnerable transitive dependencies
ThisBuild / dependencyOverrides ++= Seq(
  "com.fasterxml.jackson.core" % "jackson-core" % "2.15.0",  // CVE-2025-52999
  "com.fasterxml.jackson.core" % "jackson-databind" % "2.12.7.1, 2.13.4",  // CVE-2022-42004
  "com.google.code.gson" % "gson" % "2.8.9",  // CVE-2022-25647
  "com.google.protobuf" % "protobuf-java" % "3.25.5, 4.27.5, 4.28.2",  // CVE-2024-7254
  "com.typesafe.akka" % "akka-http-core_2.13" % "10.1.15, 10.2.7",  // CVE-2021-42697
  "io.grpc" % "grpc-netty-shaded" % "1.75.0",  // CVE-2025-55163
  "org.scala-lang" % "scala-library" % "2.13.9",  // CVE-2022-36944
  "ch.qos.logback" % "logback-classic" % "1.3.12, 1.4.12, 1.2.13",  // CVE-2023-6378
  "ch.qos.logback" % "logback-core" % "1.3.12, 1.4.12, 1.2.13",  // CVE-2023-6378
  "io.netty" % "netty-codec" % "4.1.68.Final",  // CVE-2021-37137
)
