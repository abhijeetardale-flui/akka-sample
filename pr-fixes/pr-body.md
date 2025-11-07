# 🔒 Automated Security Fixes: CRITICAL & HIGH Issues

This PR automatically addresses **69 CRITICAL and HIGH severity security issues** detected by automated security scanning.

## 📊 Issue Breakdown

| Type | Count | Description |
|------|-------|-------------|
| 🔴 **CRITICAL** | 8 | Immediate action required |
| 🟠 **HIGH** | 61 | High priority fixes |
| 📦 **SCA** (Dependencies) | 69 | Third-party library vulnerabilities |
| 🔍 **SAST** (Code) | 0 | Code-level security issues |

---

## 🔴 CRITICAL Severity Issues


### CVE-2022-36944: scala: deserialization gadget chain
- **Package:** `org.scala-lang:scala-library`
- **Current Version:** 2.13.8
- **Fixed Version:** 2.13.9
- **Type:** Software Composition Analysis (SCA)
- **Description:** Scala 2.13.x before 2.13.9 has a Java deserialization chain in its JAR file. On its own, it cannot be exploited. There is only a risk in conjunction with Java object deserialization within an applicat
- **✅ Auto-fixed:** Updated to secure version


### CVE-2022-36944: scala: deserialization gadget chain
- **Package:** `org.scala-lang:scala-library`
- **Current Version:** 2.13.8
- **Fixed Version:** 2.13.9
- **Type:** Software Composition Analysis (SCA)
- **Description:** Scala 2.13.x before 2.13.9 has a Java deserialization chain in its JAR file. On its own, it cannot be exploited. There is only a risk in conjunction with Java object deserialization within an applicat
- **✅ Auto-fixed:** Updated to secure version


### CVE-2022-36944: scala: deserialization gadget chain
- **Package:** `org.scala-lang:scala-library`
- **Current Version:** 2.13.8
- **Fixed Version:** 2.13.9
- **Type:** Software Composition Analysis (SCA)
- **Description:** Scala 2.13.x before 2.13.9 has a Java deserialization chain in its JAR file. On its own, it cannot be exploited. There is only a risk in conjunction with Java object deserialization within an applicat
- **✅ Auto-fixed:** Updated to secure version


### CVE-2022-36944: scala: deserialization gadget chain
- **Package:** `org.scala-lang:scala-library`
- **Current Version:** 2.13.8
- **Fixed Version:** 2.13.9
- **Type:** Software Composition Analysis (SCA)
- **Description:** Scala 2.13.x before 2.13.9 has a Java deserialization chain in its JAR file. On its own, it cannot be exploited. There is only a risk in conjunction with Java object deserialization within an applicat
- **✅ Auto-fixed:** Updated to secure version


### CVE-2022-36944: scala: deserialization gadget chain
- **Package:** `org.scala-lang:scala-library`
- **Current Version:** 2.13.8
- **Fixed Version:** 2.13.9
- **Type:** Software Composition Analysis (SCA)
- **Description:** Scala 2.13.x before 2.13.9 has a Java deserialization chain in its JAR file. On its own, it cannot be exploited. There is only a risk in conjunction with Java object deserialization within an applicat
- **✅ Auto-fixed:** Updated to secure version


### CVE-2022-36944: scala: deserialization gadget chain
- **Package:** `org.scala-lang:scala-library`
- **Current Version:** 2.13.8
- **Fixed Version:** 2.13.9
- **Type:** Software Composition Analysis (SCA)
- **Description:** Scala 2.13.x before 2.13.9 has a Java deserialization chain in its JAR file. On its own, it cannot be exploited. There is only a risk in conjunction with Java object deserialization within an applicat
- **✅ Auto-fixed:** Updated to secure version


### CVE-2022-36944: scala: deserialization gadget chain
- **Package:** `org.scala-lang:scala-library`
- **Current Version:** 2.13.8
- **Fixed Version:** 2.13.9
- **Type:** Software Composition Analysis (SCA)
- **Description:** Scala 2.13.x before 2.13.9 has a Java deserialization chain in its JAR file. On its own, it cannot be exploited. There is only a risk in conjunction with Java object deserialization within an applicat
- **✅ Auto-fixed:** Updated to secure version


### CVE-2022-36944: scala: deserialization gadget chain
- **Package:** `org.scala-lang:scala-library`
- **Current Version:** 2.13.8
- **Fixed Version:** 2.13.9
- **Type:** Software Composition Analysis (SCA)
- **Description:** Scala 2.13.x before 2.13.9 has a Java deserialization chain in its JAR file. On its own, it cannot be exploited. There is only a risk in conjunction with Java object deserialization within an applicat
- **✅ Auto-fixed:** Updated to secure version

---

## 🟠 HIGH Severity Issues


### CVE-2025-52999: com.fasterxml.jackson.core/jackson-core: jackson-core Potential StackoverflowErr
- **Package:** `com.fasterxml.jackson.core:jackson-core`
- **Current Version:** 2.11.4
- **Fixed Version:** 2.15.0
- **Type:** Software Composition Analysis (SCA)
- **Description:** jackson-core contains core low-level incremental ("streaming") parser and generator abstractions used by Jackson Data Processor. In versions prior to 2.15.0, if a user parses an input file and it has 
- **✅ Auto-fixed:** Updated to secure version


### CVE-2020-36518: jackson-databind: denial of service via a large depth of nested objects
- **Package:** `com.fasterxml.jackson.core:jackson-databind`
- **Current Version:** 2.11.4
- **Fixed Version:** 2.13.2.1, 2.12.6.1
- **Type:** Software Composition Analysis (SCA)
- **Description:** jackson-databind before 2.13.0 allows a Java StackOverflow exception and denial of service via a large depth of nested objects.
- **✅ Auto-fixed:** Updated to secure version


### CVE-2021-46877: jackson-databind: Possible DoS if using JDK serialization to serialize JsonNode
- **Package:** `com.fasterxml.jackson.core:jackson-databind`
- **Current Version:** 2.11.4
- **Fixed Version:** 2.12.6, 2.13.1
- **Type:** Software Composition Analysis (SCA)
- **Description:** jackson-databind 2.10.x through 2.12.x before 2.12.6 and 2.13.x before 2.13.1 allows attackers to cause a denial of service (2 GB transient heap usage per read) in uncommon situations involving JsonNo
- **✅ Auto-fixed:** Updated to secure version


### CVE-2022-42003: jackson-databind: deep wrapper array nesting wrt UNWRAP_SINGLE_VALUE_ARRAYS
- **Package:** `com.fasterxml.jackson.core:jackson-databind`
- **Current Version:** 2.11.4
- **Fixed Version:** 2.12.7.1, 2.13.4.2
- **Type:** Software Composition Analysis (SCA)
- **Description:** In FasterXML jackson-databind before versions 2.13.4.1 and 2.12.17.1, resource exhaustion can occur because of a lack of a check in primitive value deserializers to avoid deep wrapper array nesting, w
- **✅ Auto-fixed:** Updated to secure version


### CVE-2022-42004: jackson-databind: use of deeply nested arrays
- **Package:** `com.fasterxml.jackson.core:jackson-databind`
- **Current Version:** 2.11.4
- **Fixed Version:** 2.12.7.1, 2.13.4
- **Type:** Software Composition Analysis (SCA)
- **Description:** In FasterXML jackson-databind before 2.13.4, resource exhaustion can occur because of a lack of a check in BeanDeserializer._deserializeFromArray to prevent use of deeply nested arrays. An application
- **✅ Auto-fixed:** Updated to secure version


### CVE-2022-25647: com.google.code.gson-gson: Deserialization of Untrusted Data in com.google.code.
- **Package:** `com.google.code.gson:gson`
- **Current Version:** 2.8.6
- **Fixed Version:** 2.8.9
- **Type:** Software Composition Analysis (SCA)
- **Description:** The package com.google.code.gson:gson before 2.8.9 are vulnerable to Deserialization of Untrusted Data via the writeReplace() method in internal classes, which may lead to DoS attacks.
- **✅ Auto-fixed:** Updated to secure version


### CVE-2021-22569: protobuf-java: potential DoS in the parsing procedure for binary data
- **Package:** `com.google.protobuf:protobuf-java`
- **Current Version:** 3.11.4
- **Fixed Version:** 3.16.1, 3.18.2, 3.19.2
- **Type:** Software Composition Analysis (SCA)
- **Description:** An issue in protobuf-java allowed the interleaving of com.google.protobuf.UnknownFieldSet fields in such a way that would be processed out of order. A small malicious payload can occupy the parser for
- **✅ Auto-fixed:** Updated to secure version


### CVE-2022-3509: protobuf-java: Textformat parsing issue leads to DoS
- **Package:** `com.google.protobuf:protobuf-java`
- **Current Version:** 3.11.4
- **Fixed Version:** 3.16.3, 3.19.6, 3.20.3, 3.21.7
- **Type:** Software Composition Analysis (SCA)
- **Description:** A parsing issue similar to CVE-2022-3171, but with textformat in protobuf-java core and lite versions prior to 3.21.7, 3.20.3, 3.19.6 and 3.16.3 can lead to a denial of service attack. Inputs containi
- **✅ Auto-fixed:** Updated to secure version


### CVE-2022-3510: protobuf-java: Message-Type Extensions parsing issue leads to DoS
- **Package:** `com.google.protobuf:protobuf-java`
- **Current Version:** 3.11.4
- **Fixed Version:** 3.16.3, 3.19.6, 3.20.3, 3.21.7
- **Type:** Software Composition Analysis (SCA)
- **Description:** A parsing issue similar to CVE-2022-3171, but with Message-Type Extensions in protobuf-java core and lite versions prior to 3.21.7, 3.20.3, 3.19.6 and 3.16.3 can lead to a denial of service attack. In
- **✅ Auto-fixed:** Updated to secure version


### CVE-2024-7254: protobuf: StackOverflow vulnerability in Protocol Buffers
- **Package:** `com.google.protobuf:protobuf-java`
- **Current Version:** 3.11.4
- **Fixed Version:** 3.25.5, 4.27.5, 4.28.2
- **Type:** Software Composition Analysis (SCA)
- **Description:** Any project that parses untrusted Protocol Buffers data containing an arbitrary number of nested groups / series of SGROUP tags can corrupted by exceeding the stack limit i.e. StackOverflow. Parsing n
- **✅ Auto-fixed:** Updated to secure version


### CVE-2021-42697: Uncontrolled Recursion in Akka HTTP
- **Package:** `com.typesafe.akka:akka-http-core_2.13`
- **Current Version:** 10.1.11
- **Fixed Version:** 10.1.15, 10.2.7
- **Type:** Software Composition Analysis (SCA)
- **Description:** Akka HTTP 10.1.x before 10.1.15 and 10.2.x before 10.2.7 can encounter stack exhaustion while parsing HTTP headers, which allows a remote attacker to conduct a Denial of Service attack by sending a Us
- **✅ Auto-fixed:** Updated to secure version


### CVE-2025-55163: netty: netty-codec-http2: Netty MadeYouReset HTTP/2 DDoS Vulnerability
- **Package:** `io.grpc:grpc-netty-shaded`
- **Current Version:** 1.28.1
- **Fixed Version:** 1.75.0
- **Type:** Software Composition Analysis (SCA)
- **Description:** Netty is an asynchronous, event-driven network application framework. Prior to versions 4.1.124.Final and 4.2.4.Final, Netty is vulnerable to MadeYouReset DDoS. This is a logical vulnerability in the 
- **✅ Auto-fixed:** Updated to secure version


### CVE-2023-6378: logback: serialization vulnerability in logback receiver
- **Package:** `ch.qos.logback:logback-classic`
- **Current Version:** 1.2.11
- **Fixed Version:** 1.3.12, 1.4.12, 1.2.13
- **Type:** Software Composition Analysis (SCA)
- **Description:** A serialization vulnerability in logback receiver component part of 
logback version 1.4.11 allows an attacker to mount a Denial-Of-Service 
attack by sending poisoned data.


- **✅ Auto-fixed:** Updated to secure version


### CVE-2023-6378: logback: serialization vulnerability in logback receiver
- **Package:** `ch.qos.logback:logback-core`
- **Current Version:** 1.2.11
- **Fixed Version:** 1.3.12, 1.4.12, 1.2.13
- **Type:** Software Composition Analysis (SCA)
- **Description:** A serialization vulnerability in logback receiver component part of 
logback version 1.4.11 allows an attacker to mount a Denial-Of-Service 
attack by sending poisoned data.


- **✅ Auto-fixed:** Updated to secure version


### CVE-2025-52999: com.fasterxml.jackson.core/jackson-core: jackson-core Potential StackoverflowErr
- **Package:** `com.fasterxml.jackson.core:jackson-core`
- **Current Version:** 2.11.4
- **Fixed Version:** 2.15.0
- **Type:** Software Composition Analysis (SCA)
- **Description:** jackson-core contains core low-level incremental ("streaming") parser and generator abstractions used by Jackson Data Processor. In versions prior to 2.15.0, if a user parses an input file and it has 
- **✅ Auto-fixed:** Updated to secure version


### CVE-2020-36518: jackson-databind: denial of service via a large depth of nested objects
- **Package:** `com.fasterxml.jackson.core:jackson-databind`
- **Current Version:** 2.11.4
- **Fixed Version:** 2.13.2.1, 2.12.6.1
- **Type:** Software Composition Analysis (SCA)
- **Description:** jackson-databind before 2.13.0 allows a Java StackOverflow exception and denial of service via a large depth of nested objects.
- **✅ Auto-fixed:** Updated to secure version


### CVE-2021-46877: jackson-databind: Possible DoS if using JDK serialization to serialize JsonNode
- **Package:** `com.fasterxml.jackson.core:jackson-databind`
- **Current Version:** 2.11.4
- **Fixed Version:** 2.12.6, 2.13.1
- **Type:** Software Composition Analysis (SCA)
- **Description:** jackson-databind 2.10.x through 2.12.x before 2.12.6 and 2.13.x before 2.13.1 allows attackers to cause a denial of service (2 GB transient heap usage per read) in uncommon situations involving JsonNo
- **✅ Auto-fixed:** Updated to secure version


### CVE-2022-42003: jackson-databind: deep wrapper array nesting wrt UNWRAP_SINGLE_VALUE_ARRAYS
- **Package:** `com.fasterxml.jackson.core:jackson-databind`
- **Current Version:** 2.11.4
- **Fixed Version:** 2.12.7.1, 2.13.4.2
- **Type:** Software Composition Analysis (SCA)
- **Description:** In FasterXML jackson-databind before versions 2.13.4.1 and 2.12.17.1, resource exhaustion can occur because of a lack of a check in primitive value deserializers to avoid deep wrapper array nesting, w
- **✅ Auto-fixed:** Updated to secure version


### CVE-2022-42004: jackson-databind: use of deeply nested arrays
- **Package:** `com.fasterxml.jackson.core:jackson-databind`
- **Current Version:** 2.11.4
- **Fixed Version:** 2.12.7.1, 2.13.4
- **Type:** Software Composition Analysis (SCA)
- **Description:** In FasterXML jackson-databind before 2.13.4, resource exhaustion can occur because of a lack of a check in BeanDeserializer._deserializeFromArray to prevent use of deeply nested arrays. An application
- **✅ Auto-fixed:** Updated to secure version


### CVE-2023-6378: logback: serialization vulnerability in logback receiver
- **Package:** `ch.qos.logback:logback-classic`
- **Current Version:** 1.2.11
- **Fixed Version:** 1.3.12, 1.4.12, 1.2.13
- **Type:** Software Composition Analysis (SCA)
- **Description:** A serialization vulnerability in logback receiver component part of 
logback version 1.4.11 allows an attacker to mount a Denial-Of-Service 
attack by sending poisoned data.


- **✅ Auto-fixed:** Updated to secure version


### CVE-2023-6378: logback: serialization vulnerability in logback receiver
- **Package:** `ch.qos.logback:logback-core`
- **Current Version:** 1.2.11
- **Fixed Version:** 1.3.12, 1.4.12, 1.2.13
- **Type:** Software Composition Analysis (SCA)
- **Description:** A serialization vulnerability in logback receiver component part of 
logback version 1.4.11 allows an attacker to mount a Denial-Of-Service 
attack by sending poisoned data.


- **✅ Auto-fixed:** Updated to secure version


### CVE-2023-6378: logback: serialization vulnerability in logback receiver
- **Package:** `ch.qos.logback:logback-classic`
- **Current Version:** 1.2.11
- **Fixed Version:** 1.3.12, 1.4.12, 1.2.13
- **Type:** Software Composition Analysis (SCA)
- **Description:** A serialization vulnerability in logback receiver component part of 
logback version 1.4.11 allows an attacker to mount a Denial-Of-Service 
attack by sending poisoned data.


- **✅ Auto-fixed:** Updated to secure version


### CVE-2023-6378: logback: serialization vulnerability in logback receiver
- **Package:** `ch.qos.logback:logback-core`
- **Current Version:** 1.2.11
- **Fixed Version:** 1.3.12, 1.4.12, 1.2.13
- **Type:** Software Composition Analysis (SCA)
- **Description:** A serialization vulnerability in logback receiver component part of 
logback version 1.4.11 allows an attacker to mount a Denial-Of-Service 
attack by sending poisoned data.


- **✅ Auto-fixed:** Updated to secure version


### CVE-2025-52999: com.fasterxml.jackson.core/jackson-core: jackson-core Potential StackoverflowErr
- **Package:** `com.fasterxml.jackson.core:jackson-core`
- **Current Version:** 2.11.4
- **Fixed Version:** 2.15.0
- **Type:** Software Composition Analysis (SCA)
- **Description:** jackson-core contains core low-level incremental ("streaming") parser and generator abstractions used by Jackson Data Processor. In versions prior to 2.15.0, if a user parses an input file and it has 
- **✅ Auto-fixed:** Updated to secure version


### CVE-2020-36518: jackson-databind: denial of service via a large depth of nested objects
- **Package:** `com.fasterxml.jackson.core:jackson-databind`
- **Current Version:** 2.11.4
- **Fixed Version:** 2.13.2.1, 2.12.6.1
- **Type:** Software Composition Analysis (SCA)
- **Description:** jackson-databind before 2.13.0 allows a Java StackOverflow exception and denial of service via a large depth of nested objects.
- **✅ Auto-fixed:** Updated to secure version


### CVE-2021-46877: jackson-databind: Possible DoS if using JDK serialization to serialize JsonNode
- **Package:** `com.fasterxml.jackson.core:jackson-databind`
- **Current Version:** 2.11.4
- **Fixed Version:** 2.12.6, 2.13.1
- **Type:** Software Composition Analysis (SCA)
- **Description:** jackson-databind 2.10.x through 2.12.x before 2.12.6 and 2.13.x before 2.13.1 allows attackers to cause a denial of service (2 GB transient heap usage per read) in uncommon situations involving JsonNo
- **✅ Auto-fixed:** Updated to secure version


### CVE-2022-42003: jackson-databind: deep wrapper array nesting wrt UNWRAP_SINGLE_VALUE_ARRAYS
- **Package:** `com.fasterxml.jackson.core:jackson-databind`
- **Current Version:** 2.11.4
- **Fixed Version:** 2.12.7.1, 2.13.4.2
- **Type:** Software Composition Analysis (SCA)
- **Description:** In FasterXML jackson-databind before versions 2.13.4.1 and 2.12.17.1, resource exhaustion can occur because of a lack of a check in primitive value deserializers to avoid deep wrapper array nesting, w
- **✅ Auto-fixed:** Updated to secure version


### CVE-2022-42004: jackson-databind: use of deeply nested arrays
- **Package:** `com.fasterxml.jackson.core:jackson-databind`
- **Current Version:** 2.11.4
- **Fixed Version:** 2.12.7.1, 2.13.4
- **Type:** Software Composition Analysis (SCA)
- **Description:** In FasterXML jackson-databind before 2.13.4, resource exhaustion can occur because of a lack of a check in BeanDeserializer._deserializeFromArray to prevent use of deeply nested arrays. An application
- **✅ Auto-fixed:** Updated to secure version


### CVE-2021-37136: netty-codec: Bzip2Decoder doesn't allow setting size restrictions for decompress
- **Package:** `io.netty:netty-codec`
- **Current Version:** 4.1.52.Final
- **Fixed Version:** 4.1.68.Final
- **Type:** Software Composition Analysis (SCA)
- **Description:** The Bzip2 decompression decoder function doesn't allow setting size restrictions on the decompressed output data (which affects the allocation size used during decompression). All users of Bzip2Decode
- **✅ Auto-fixed:** Updated to secure version


### CVE-2021-37137: netty-codec: SnappyFrameDecoder doesn't restrict chunk length and may buffer ski
- **Package:** `io.netty:netty-codec`
- **Current Version:** 4.1.52.Final
- **Fixed Version:** 4.1.68.Final
- **Type:** Software Composition Analysis (SCA)
- **Description:** The Snappy frame decoder function doesn't restrict the chunk length which may lead to excessive memory usage. Beside this it also may buffer reserved skippable chunks until the whole chunk was receive
- **✅ Auto-fixed:** Updated to secure version


### CVE-2023-6378: logback: serialization vulnerability in logback receiver
- **Package:** `ch.qos.logback:logback-classic`
- **Current Version:** 1.2.11
- **Fixed Version:** 1.3.12, 1.4.12, 1.2.13
- **Type:** Software Composition Analysis (SCA)
- **Description:** A serialization vulnerability in logback receiver component part of 
logback version 1.4.11 allows an attacker to mount a Denial-Of-Service 
attack by sending poisoned data.


- **✅ Auto-fixed:** Updated to secure version


### CVE-2023-6378: logback: serialization vulnerability in logback receiver
- **Package:** `ch.qos.logback:logback-core`
- **Current Version:** 1.2.11
- **Fixed Version:** 1.3.12, 1.4.12, 1.2.13
- **Type:** Software Composition Analysis (SCA)
- **Description:** A serialization vulnerability in logback receiver component part of 
logback version 1.4.11 allows an attacker to mount a Denial-Of-Service 
attack by sending poisoned data.


- **✅ Auto-fixed:** Updated to secure version


### CVE-2025-52999: com.fasterxml.jackson.core/jackson-core: jackson-core Potential StackoverflowErr
- **Package:** `com.fasterxml.jackson.core:jackson-core`
- **Current Version:** 2.11.4
- **Fixed Version:** 2.15.0
- **Type:** Software Composition Analysis (SCA)
- **Description:** jackson-core contains core low-level incremental ("streaming") parser and generator abstractions used by Jackson Data Processor. In versions prior to 2.15.0, if a user parses an input file and it has 
- **✅ Auto-fixed:** Updated to secure version


### CVE-2020-36518: jackson-databind: denial of service via a large depth of nested objects
- **Package:** `com.fasterxml.jackson.core:jackson-databind`
- **Current Version:** 2.11.4
- **Fixed Version:** 2.13.2.1, 2.12.6.1
- **Type:** Software Composition Analysis (SCA)
- **Description:** jackson-databind before 2.13.0 allows a Java StackOverflow exception and denial of service via a large depth of nested objects.
- **✅ Auto-fixed:** Updated to secure version


### CVE-2021-46877: jackson-databind: Possible DoS if using JDK serialization to serialize JsonNode
- **Package:** `com.fasterxml.jackson.core:jackson-databind`
- **Current Version:** 2.11.4
- **Fixed Version:** 2.12.6, 2.13.1
- **Type:** Software Composition Analysis (SCA)
- **Description:** jackson-databind 2.10.x through 2.12.x before 2.12.6 and 2.13.x before 2.13.1 allows attackers to cause a denial of service (2 GB transient heap usage per read) in uncommon situations involving JsonNo
- **✅ Auto-fixed:** Updated to secure version


### CVE-2022-42003: jackson-databind: deep wrapper array nesting wrt UNWRAP_SINGLE_VALUE_ARRAYS
- **Package:** `com.fasterxml.jackson.core:jackson-databind`
- **Current Version:** 2.11.4
- **Fixed Version:** 2.12.7.1, 2.13.4.2
- **Type:** Software Composition Analysis (SCA)
- **Description:** In FasterXML jackson-databind before versions 2.13.4.1 and 2.12.17.1, resource exhaustion can occur because of a lack of a check in primitive value deserializers to avoid deep wrapper array nesting, w
- **✅ Auto-fixed:** Updated to secure version


### CVE-2022-42004: jackson-databind: use of deeply nested arrays
- **Package:** `com.fasterxml.jackson.core:jackson-databind`
- **Current Version:** 2.11.4
- **Fixed Version:** 2.12.7.1, 2.13.4
- **Type:** Software Composition Analysis (SCA)
- **Description:** In FasterXML jackson-databind before 2.13.4, resource exhaustion can occur because of a lack of a check in BeanDeserializer._deserializeFromArray to prevent use of deeply nested arrays. An application
- **✅ Auto-fixed:** Updated to secure version


### CVE-2023-6378: logback: serialization vulnerability in logback receiver
- **Package:** `ch.qos.logback:logback-classic`
- **Current Version:** 1.2.11
- **Fixed Version:** 1.3.12, 1.4.12, 1.2.13
- **Type:** Software Composition Analysis (SCA)
- **Description:** A serialization vulnerability in logback receiver component part of 
logback version 1.4.11 allows an attacker to mount a Denial-Of-Service 
attack by sending poisoned data.


- **✅ Auto-fixed:** Updated to secure version


### CVE-2023-6378: logback: serialization vulnerability in logback receiver
- **Package:** `ch.qos.logback:logback-core`
- **Current Version:** 1.2.11
- **Fixed Version:** 1.3.12, 1.4.12, 1.2.13
- **Type:** Software Composition Analysis (SCA)
- **Description:** A serialization vulnerability in logback receiver component part of 
logback version 1.4.11 allows an attacker to mount a Denial-Of-Service 
attack by sending poisoned data.


- **✅ Auto-fixed:** Updated to secure version


### CVE-2025-52999: com.fasterxml.jackson.core/jackson-core: jackson-core Potential StackoverflowErr
- **Package:** `com.fasterxml.jackson.core:jackson-core`
- **Current Version:** 2.11.4
- **Fixed Version:** 2.15.0
- **Type:** Software Composition Analysis (SCA)
- **Description:** jackson-core contains core low-level incremental ("streaming") parser and generator abstractions used by Jackson Data Processor. In versions prior to 2.15.0, if a user parses an input file and it has 
- **✅ Auto-fixed:** Updated to secure version


### CVE-2020-36518: jackson-databind: denial of service via a large depth of nested objects
- **Package:** `com.fasterxml.jackson.core:jackson-databind`
- **Current Version:** 2.11.4
- **Fixed Version:** 2.13.2.1, 2.12.6.1
- **Type:** Software Composition Analysis (SCA)
- **Description:** jackson-databind before 2.13.0 allows a Java StackOverflow exception and denial of service via a large depth of nested objects.
- **✅ Auto-fixed:** Updated to secure version


### CVE-2021-46877: jackson-databind: Possible DoS if using JDK serialization to serialize JsonNode
- **Package:** `com.fasterxml.jackson.core:jackson-databind`
- **Current Version:** 2.11.4
- **Fixed Version:** 2.12.6, 2.13.1
- **Type:** Software Composition Analysis (SCA)
- **Description:** jackson-databind 2.10.x through 2.12.x before 2.12.6 and 2.13.x before 2.13.1 allows attackers to cause a denial of service (2 GB transient heap usage per read) in uncommon situations involving JsonNo
- **✅ Auto-fixed:** Updated to secure version


### CVE-2022-42003: jackson-databind: deep wrapper array nesting wrt UNWRAP_SINGLE_VALUE_ARRAYS
- **Package:** `com.fasterxml.jackson.core:jackson-databind`
- **Current Version:** 2.11.4
- **Fixed Version:** 2.12.7.1, 2.13.4.2
- **Type:** Software Composition Analysis (SCA)
- **Description:** In FasterXML jackson-databind before versions 2.13.4.1 and 2.12.17.1, resource exhaustion can occur because of a lack of a check in primitive value deserializers to avoid deep wrapper array nesting, w
- **✅ Auto-fixed:** Updated to secure version


### CVE-2022-42004: jackson-databind: use of deeply nested arrays
- **Package:** `com.fasterxml.jackson.core:jackson-databind`
- **Current Version:** 2.11.4
- **Fixed Version:** 2.12.7.1, 2.13.4
- **Type:** Software Composition Analysis (SCA)
- **Description:** In FasterXML jackson-databind before 2.13.4, resource exhaustion can occur because of a lack of a check in BeanDeserializer._deserializeFromArray to prevent use of deeply nested arrays. An application
- **✅ Auto-fixed:** Updated to secure version


### CVE-2021-42697: Uncontrolled Recursion in Akka HTTP
- **Package:** `com.typesafe.akka:akka-http-core_2.13`
- **Current Version:** 10.1.11
- **Fixed Version:** 10.1.15, 10.2.7
- **Type:** Software Composition Analysis (SCA)
- **Description:** Akka HTTP 10.1.x before 10.1.15 and 10.2.x before 10.2.7 can encounter stack exhaustion while parsing HTTP headers, which allows a remote attacker to conduct a Denial of Service attack by sending a Us
- **✅ Auto-fixed:** Updated to secure version


### CVE-2023-6378: logback: serialization vulnerability in logback receiver
- **Package:** `ch.qos.logback:logback-classic`
- **Current Version:** 1.2.11
- **Fixed Version:** 1.3.12, 1.4.12, 1.2.13
- **Type:** Software Composition Analysis (SCA)
- **Description:** A serialization vulnerability in logback receiver component part of 
logback version 1.4.11 allows an attacker to mount a Denial-Of-Service 
attack by sending poisoned data.


- **✅ Auto-fixed:** Updated to secure version


### CVE-2023-6378: logback: serialization vulnerability in logback receiver
- **Package:** `ch.qos.logback:logback-core`
- **Current Version:** 1.2.11
- **Fixed Version:** 1.3.12, 1.4.12, 1.2.13
- **Type:** Software Composition Analysis (SCA)
- **Description:** A serialization vulnerability in logback receiver component part of 
logback version 1.4.11 allows an attacker to mount a Denial-Of-Service 
attack by sending poisoned data.


- **✅ Auto-fixed:** Updated to secure version


### CVE-2025-52999: com.fasterxml.jackson.core/jackson-core: jackson-core Potential StackoverflowErr
- **Package:** `com.fasterxml.jackson.core:jackson-core`
- **Current Version:** 2.11.4
- **Fixed Version:** 2.15.0
- **Type:** Software Composition Analysis (SCA)
- **Description:** jackson-core contains core low-level incremental ("streaming") parser and generator abstractions used by Jackson Data Processor. In versions prior to 2.15.0, if a user parses an input file and it has 
- **✅ Auto-fixed:** Updated to secure version


### CVE-2020-36518: jackson-databind: denial of service via a large depth of nested objects
- **Package:** `com.fasterxml.jackson.core:jackson-databind`
- **Current Version:** 2.11.4
- **Fixed Version:** 2.13.2.1, 2.12.6.1
- **Type:** Software Composition Analysis (SCA)
- **Description:** jackson-databind before 2.13.0 allows a Java StackOverflow exception and denial of service via a large depth of nested objects.
- **✅ Auto-fixed:** Updated to secure version


### CVE-2021-46877: jackson-databind: Possible DoS if using JDK serialization to serialize JsonNode
- **Package:** `com.fasterxml.jackson.core:jackson-databind`
- **Current Version:** 2.11.4
- **Fixed Version:** 2.12.6, 2.13.1
- **Type:** Software Composition Analysis (SCA)
- **Description:** jackson-databind 2.10.x through 2.12.x before 2.12.6 and 2.13.x before 2.13.1 allows attackers to cause a denial of service (2 GB transient heap usage per read) in uncommon situations involving JsonNo
- **✅ Auto-fixed:** Updated to secure version


### CVE-2022-42003: jackson-databind: deep wrapper array nesting wrt UNWRAP_SINGLE_VALUE_ARRAYS
- **Package:** `com.fasterxml.jackson.core:jackson-databind`
- **Current Version:** 2.11.4
- **Fixed Version:** 2.12.7.1, 2.13.4.2
- **Type:** Software Composition Analysis (SCA)
- **Description:** In FasterXML jackson-databind before versions 2.13.4.1 and 2.12.17.1, resource exhaustion can occur because of a lack of a check in primitive value deserializers to avoid deep wrapper array nesting, w
- **✅ Auto-fixed:** Updated to secure version


### CVE-2022-42004: jackson-databind: use of deeply nested arrays
- **Package:** `com.fasterxml.jackson.core:jackson-databind`
- **Current Version:** 2.11.4
- **Fixed Version:** 2.12.7.1, 2.13.4
- **Type:** Software Composition Analysis (SCA)
- **Description:** In FasterXML jackson-databind before 2.13.4, resource exhaustion can occur because of a lack of a check in BeanDeserializer._deserializeFromArray to prevent use of deeply nested arrays. An application
- **✅ Auto-fixed:** Updated to secure version


### CVE-2021-42697: Uncontrolled Recursion in Akka HTTP
- **Package:** `com.typesafe.akka:akka-http-core_2.13`
- **Current Version:** 10.1.11
- **Fixed Version:** 10.1.15, 10.2.7
- **Type:** Software Composition Analysis (SCA)
- **Description:** Akka HTTP 10.1.x before 10.1.15 and 10.2.x before 10.2.7 can encounter stack exhaustion while parsing HTTP headers, which allows a remote attacker to conduct a Denial of Service attack by sending a Us
- **✅ Auto-fixed:** Updated to secure version


### CVE-2023-6378: logback: serialization vulnerability in logback receiver
- **Package:** `ch.qos.logback:logback-classic`
- **Current Version:** 1.2.11
- **Fixed Version:** 1.3.12, 1.4.12, 1.2.13
- **Type:** Software Composition Analysis (SCA)
- **Description:** A serialization vulnerability in logback receiver component part of 
logback version 1.4.11 allows an attacker to mount a Denial-Of-Service 
attack by sending poisoned data.


- **✅ Auto-fixed:** Updated to secure version


### CVE-2023-6378: logback: serialization vulnerability in logback receiver
- **Package:** `ch.qos.logback:logback-core`
- **Current Version:** 1.2.11
- **Fixed Version:** 1.3.12, 1.4.12, 1.2.13
- **Type:** Software Composition Analysis (SCA)
- **Description:** A serialization vulnerability in logback receiver component part of 
logback version 1.4.11 allows an attacker to mount a Denial-Of-Service 
attack by sending poisoned data.


- **✅ Auto-fixed:** Updated to secure version


### CVE-2025-52999: com.fasterxml.jackson.core/jackson-core: jackson-core Potential StackoverflowErr
- **Package:** `com.fasterxml.jackson.core:jackson-core`
- **Current Version:** 2.11.4
- **Fixed Version:** 2.15.0
- **Type:** Software Composition Analysis (SCA)
- **Description:** jackson-core contains core low-level incremental ("streaming") parser and generator abstractions used by Jackson Data Processor. In versions prior to 2.15.0, if a user parses an input file and it has 
- **✅ Auto-fixed:** Updated to secure version


### CVE-2020-36518: jackson-databind: denial of service via a large depth of nested objects
- **Package:** `com.fasterxml.jackson.core:jackson-databind`
- **Current Version:** 2.11.4
- **Fixed Version:** 2.13.2.1, 2.12.6.1
- **Type:** Software Composition Analysis (SCA)
- **Description:** jackson-databind before 2.13.0 allows a Java StackOverflow exception and denial of service via a large depth of nested objects.
- **✅ Auto-fixed:** Updated to secure version


### CVE-2021-46877: jackson-databind: Possible DoS if using JDK serialization to serialize JsonNode
- **Package:** `com.fasterxml.jackson.core:jackson-databind`
- **Current Version:** 2.11.4
- **Fixed Version:** 2.12.6, 2.13.1
- **Type:** Software Composition Analysis (SCA)
- **Description:** jackson-databind 2.10.x through 2.12.x before 2.12.6 and 2.13.x before 2.13.1 allows attackers to cause a denial of service (2 GB transient heap usage per read) in uncommon situations involving JsonNo
- **✅ Auto-fixed:** Updated to secure version


### CVE-2022-42003: jackson-databind: deep wrapper array nesting wrt UNWRAP_SINGLE_VALUE_ARRAYS
- **Package:** `com.fasterxml.jackson.core:jackson-databind`
- **Current Version:** 2.11.4
- **Fixed Version:** 2.12.7.1, 2.13.4.2
- **Type:** Software Composition Analysis (SCA)
- **Description:** In FasterXML jackson-databind before versions 2.13.4.1 and 2.12.17.1, resource exhaustion can occur because of a lack of a check in primitive value deserializers to avoid deep wrapper array nesting, w
- **✅ Auto-fixed:** Updated to secure version


### CVE-2022-42004: jackson-databind: use of deeply nested arrays
- **Package:** `com.fasterxml.jackson.core:jackson-databind`
- **Current Version:** 2.11.4
- **Fixed Version:** 2.12.7.1, 2.13.4
- **Type:** Software Composition Analysis (SCA)
- **Description:** In FasterXML jackson-databind before 2.13.4, resource exhaustion can occur because of a lack of a check in BeanDeserializer._deserializeFromArray to prevent use of deeply nested arrays. An application
- **✅ Auto-fixed:** Updated to secure version


### CVE-2021-42697: Uncontrolled Recursion in Akka HTTP
- **Package:** `com.typesafe.akka:akka-http-core_2.13`
- **Current Version:** 10.1.11
- **Fixed Version:** 10.1.15, 10.2.7
- **Type:** Software Composition Analysis (SCA)
- **Description:** Akka HTTP 10.1.x before 10.1.15 and 10.2.x before 10.2.7 can encounter stack exhaustion while parsing HTTP headers, which allows a remote attacker to conduct a Denial of Service attack by sending a Us
- **✅ Auto-fixed:** Updated to secure version

---

## ✅ What Was Fixed Automatically

This PR includes **automatic fixes** for:
- ✅ **69 SCA (dependency) vulnerabilities** - Updated to secure versions
- ⚠️ **0 SAST (code) issues** - Identified for manual review

### Automatic Dependency Updates Applied:
- `com.fasterxml.jackson.core:jackson-core`: 2.11.4 → 2.15.0 (CVE-2025-52999)
- `com.fasterxml.jackson.core:jackson-databind`: 2.11.4 → 2.13.2.1, 2.12.6.1 (CVE-2020-36518)
- `com.fasterxml.jackson.core:jackson-databind`: 2.11.4 → 2.12.6, 2.13.1 (CVE-2021-46877)
- `com.fasterxml.jackson.core:jackson-databind`: 2.11.4 → 2.12.7.1, 2.13.4.2 (CVE-2022-42003)
- `com.fasterxml.jackson.core:jackson-databind`: 2.11.4 → 2.12.7.1, 2.13.4 (CVE-2022-42004)
- `com.google.code.gson:gson`: 2.8.6 → 2.8.9 (CVE-2022-25647)
- `com.google.protobuf:protobuf-java`: 3.11.4 → 3.16.1, 3.18.2, 3.19.2 (CVE-2021-22569)
- `com.google.protobuf:protobuf-java`: 3.11.4 → 3.16.3, 3.19.6, 3.20.3, 3.21.7 (CVE-2022-3509)
- `com.google.protobuf:protobuf-java`: 3.11.4 → 3.16.3, 3.19.6, 3.20.3, 3.21.7 (CVE-2022-3510)
- `com.google.protobuf:protobuf-java`: 3.11.4 → 3.25.5, 4.27.5, 4.28.2 (CVE-2024-7254)
- `com.typesafe.akka:akka-http-core_2.13`: 10.1.11 → 10.1.15, 10.2.7 (CVE-2021-42697)
- `io.grpc:grpc-netty-shaded`: 1.28.1 → 1.75.0 (CVE-2025-55163)
- `org.scala-lang:scala-library`: 2.13.8 → 2.13.9 (CVE-2022-36944)
- `ch.qos.logback:logback-classic`: 1.2.11 → 1.3.12, 1.4.12, 1.2.13 (CVE-2023-6378)
- `ch.qos.logback:logback-core`: 1.2.11 → 1.3.12, 1.4.12, 1.2.13 (CVE-2023-6378)
- `com.fasterxml.jackson.core:jackson-core`: 2.11.4 → 2.15.0 (CVE-2025-52999)
- `com.fasterxml.jackson.core:jackson-databind`: 2.11.4 → 2.13.2.1, 2.12.6.1 (CVE-2020-36518)
- `com.fasterxml.jackson.core:jackson-databind`: 2.11.4 → 2.12.6, 2.13.1 (CVE-2021-46877)
- `com.fasterxml.jackson.core:jackson-databind`: 2.11.4 → 2.12.7.1, 2.13.4.2 (CVE-2022-42003)
- `com.fasterxml.jackson.core:jackson-databind`: 2.11.4 → 2.12.7.1, 2.13.4 (CVE-2022-42004)
- `org.scala-lang:scala-library`: 2.13.8 → 2.13.9 (CVE-2022-36944)
- `ch.qos.logback:logback-classic`: 1.2.11 → 1.3.12, 1.4.12, 1.2.13 (CVE-2023-6378)
- `ch.qos.logback:logback-core`: 1.2.11 → 1.3.12, 1.4.12, 1.2.13 (CVE-2023-6378)
- `org.scala-lang:scala-library`: 2.13.8 → 2.13.9 (CVE-2022-36944)
- `ch.qos.logback:logback-classic`: 1.2.11 → 1.3.12, 1.4.12, 1.2.13 (CVE-2023-6378)
- `ch.qos.logback:logback-core`: 1.2.11 → 1.3.12, 1.4.12, 1.2.13 (CVE-2023-6378)
- `com.fasterxml.jackson.core:jackson-core`: 2.11.4 → 2.15.0 (CVE-2025-52999)
- `com.fasterxml.jackson.core:jackson-databind`: 2.11.4 → 2.13.2.1, 2.12.6.1 (CVE-2020-36518)
- `com.fasterxml.jackson.core:jackson-databind`: 2.11.4 → 2.12.6, 2.13.1 (CVE-2021-46877)
- `com.fasterxml.jackson.core:jackson-databind`: 2.11.4 → 2.12.7.1, 2.13.4.2 (CVE-2022-42003)
- `com.fasterxml.jackson.core:jackson-databind`: 2.11.4 → 2.12.7.1, 2.13.4 (CVE-2022-42004)
- `io.netty:netty-codec`: 4.1.52.Final → 4.1.68.Final (CVE-2021-37136)
- `io.netty:netty-codec`: 4.1.52.Final → 4.1.68.Final (CVE-2021-37137)
- `org.scala-lang:scala-library`: 2.13.8 → 2.13.9 (CVE-2022-36944)
- `ch.qos.logback:logback-classic`: 1.2.11 → 1.3.12, 1.4.12, 1.2.13 (CVE-2023-6378)
- `ch.qos.logback:logback-core`: 1.2.11 → 1.3.12, 1.4.12, 1.2.13 (CVE-2023-6378)
- `com.fasterxml.jackson.core:jackson-core`: 2.11.4 → 2.15.0 (CVE-2025-52999)
- `com.fasterxml.jackson.core:jackson-databind`: 2.11.4 → 2.13.2.1, 2.12.6.1 (CVE-2020-36518)
- `com.fasterxml.jackson.core:jackson-databind`: 2.11.4 → 2.12.6, 2.13.1 (CVE-2021-46877)
- `com.fasterxml.jackson.core:jackson-databind`: 2.11.4 → 2.12.7.1, 2.13.4.2 (CVE-2022-42003)
- `com.fasterxml.jackson.core:jackson-databind`: 2.11.4 → 2.12.7.1, 2.13.4 (CVE-2022-42004)
- `org.scala-lang:scala-library`: 2.13.8 → 2.13.9 (CVE-2022-36944)
- `ch.qos.logback:logback-classic`: 1.2.11 → 1.3.12, 1.4.12, 1.2.13 (CVE-2023-6378)
- `ch.qos.logback:logback-core`: 1.2.11 → 1.3.12, 1.4.12, 1.2.13 (CVE-2023-6378)
- `com.fasterxml.jackson.core:jackson-core`: 2.11.4 → 2.15.0 (CVE-2025-52999)
- `com.fasterxml.jackson.core:jackson-databind`: 2.11.4 → 2.13.2.1, 2.12.6.1 (CVE-2020-36518)
- `com.fasterxml.jackson.core:jackson-databind`: 2.11.4 → 2.12.6, 2.13.1 (CVE-2021-46877)
- `com.fasterxml.jackson.core:jackson-databind`: 2.11.4 → 2.12.7.1, 2.13.4.2 (CVE-2022-42003)
- `com.fasterxml.jackson.core:jackson-databind`: 2.11.4 → 2.12.7.1, 2.13.4 (CVE-2022-42004)
- `com.typesafe.akka:akka-http-core_2.13`: 10.1.11 → 10.1.15, 10.2.7 (CVE-2021-42697)
- `org.scala-lang:scala-library`: 2.13.8 → 2.13.9 (CVE-2022-36944)
- `ch.qos.logback:logback-classic`: 1.2.11 → 1.3.12, 1.4.12, 1.2.13 (CVE-2023-6378)
- `ch.qos.logback:logback-core`: 1.2.11 → 1.3.12, 1.4.12, 1.2.13 (CVE-2023-6378)
- `com.fasterxml.jackson.core:jackson-core`: 2.11.4 → 2.15.0 (CVE-2025-52999)
- `com.fasterxml.jackson.core:jackson-databind`: 2.11.4 → 2.13.2.1, 2.12.6.1 (CVE-2020-36518)
- `com.fasterxml.jackson.core:jackson-databind`: 2.11.4 → 2.12.6, 2.13.1 (CVE-2021-46877)
- `com.fasterxml.jackson.core:jackson-databind`: 2.11.4 → 2.12.7.1, 2.13.4.2 (CVE-2022-42003)
- `com.fasterxml.jackson.core:jackson-databind`: 2.11.4 → 2.12.7.1, 2.13.4 (CVE-2022-42004)
- `com.typesafe.akka:akka-http-core_2.13`: 10.1.11 → 10.1.15, 10.2.7 (CVE-2021-42697)
- `org.scala-lang:scala-library`: 2.13.8 → 2.13.9 (CVE-2022-36944)
- `ch.qos.logback:logback-classic`: 1.2.11 → 1.3.12, 1.4.12, 1.2.13 (CVE-2023-6378)
- `ch.qos.logback:logback-core`: 1.2.11 → 1.3.12, 1.4.12, 1.2.13 (CVE-2023-6378)
- `com.fasterxml.jackson.core:jackson-core`: 2.11.4 → 2.15.0 (CVE-2025-52999)
- `com.fasterxml.jackson.core:jackson-databind`: 2.11.4 → 2.13.2.1, 2.12.6.1 (CVE-2020-36518)
- `com.fasterxml.jackson.core:jackson-databind`: 2.11.4 → 2.12.6, 2.13.1 (CVE-2021-46877)
- `com.fasterxml.jackson.core:jackson-databind`: 2.11.4 → 2.12.7.1, 2.13.4.2 (CVE-2022-42003)
- `com.fasterxml.jackson.core:jackson-databind`: 2.11.4 → 2.12.7.1, 2.13.4 (CVE-2022-42004)
- `com.typesafe.akka:akka-http-core_2.13`: 10.1.11 → 10.1.15, 10.2.7 (CVE-2021-42697)
- `org.scala-lang:scala-library`: 2.13.8 → 2.13.9 (CVE-2022-36944)

### Manual Code Review Required:
_No manual code changes required._

---

## 🧪 Testing

Please verify:
1. ✅ All builds pass
2. ✅ Tests pass
3. ✅ No regressions introduced
4. ⚠️ Review SAST issues and apply fixes if needed

---

## 📚 Additional Information

- **Scan Type:** SAST + SCA (Comprehensive)
- **Severity Filter:** CRITICAL and HIGH only
- **Auto-Generated:** Yes, by security automation workflow
- **Triggered By:** workflow_dispatch

---

## 🎯 Next Steps

1. **Review this PR** - Check all changes
2. **Test thoroughly** - Ensure no breaking changes
3. **Merge when ready** - Apply security fixes
4. **Monitor** - Watch for any issues post-merge

**This is an automated security PR. Please review carefully before merging.**

---

*Generated by: Auto PR for Critical & High Vulnerabilities workflow*
*Scan Date: 19153375413*
