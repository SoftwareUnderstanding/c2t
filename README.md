# Container to triples
Container to triples: a package to convert the libraries and packages inside a container into structured information

![](https://raw.githubusercontent.com/SoftwareUnderstanding/c2t/main/images/dockerKG.png)

### Example V0.1.0 



```bash
@prefix dc: <http://purl.org/dc/elements/1.1/> .
@prefix ns1: <https://w3id.org/docker/image/#> .

<https://w3id.org/docker/image/id/sha256%3A00a819650c3d1a8edacacc964c453a8fef485751581c4d6262e035b5587b0be0> a ns1:dockerObject ;
    dc:identifier "sha256:00a819650c3d1a8edacacc964c453a8fef485751581c4d6262e035b5587b0be0" ;
    ns1:architecture "amd64" ;
    ns1:container "a24858b02c25724b682f0d2ce6713434e5cec7a95e93b37502982d766dc56426" ;
    ns1:dockerVersion "20.10.3" ;
    ns1:os "linux" ;
    ns1:size "550351730" .
```



Query:

```sql
SELECT * WHERE {
    ?s <https://w3id.org/docker/image/#os> ?os;
	   <https://w3id.org/docker/image/#architecture> ?architecture;
	   <https://w3id.org/docker/image/#container> ?container;
	   <https://w3id.org/docker/image/#dockerVersion> ?dockerVersion;
	   <https://w3id.org/docker/image/#size> ?sizeMB.

}

```

Result:

| imageID                                                      | os        | architecture | container                                                    | dockerVersion | sizeMB        |
| ------------------------------------------------------------ | --------- | ------------ | ------------------------------------------------------------ | ------------- | ------------- |
| https://w3id.org/docker/image/id/sha256%3A00a819650c3d1a8edacacc964c453a8fef485751581c4d6262e035b5587b0be0 | `"linux"` | `"amd64"`    | `"a24858b02c25724b682f0d2ce6713434e5cec7a95e93b37502982d766dc56426"` | `"20.10.3"`   | `"550351730"` |
| https://w3id.org/docker/image/id/sha256%3A37cb44321d0423bc57266a3bff658daf00478e4cdf2d3b8091f785310534256d | `"linux"` | `"amd64"`    | `"8c820295f9f76020828b7f5d35fb1199f998f4b490ea679c991f5ede1bbf4c0f"` | `"20.10.12"`  | `"407749778"` |
| https://w3id.org/docker/image/id/sha256%3A3ec53c05a84536be973b242e8bca9ffb65c8575c38faaa821e8d0f58803b10a6 | `"linux"` | `"amd64"`    | `"f578581d1b7eac923ed29d40384fa401ef2c43a51c514d513056f48328410f7f"` | `"20.10.3"`   | `"423871271"` |
| https://w3id.org/docker/image/id/sha256%3A68c90e8dafce6c4e4a9825ca975dfde61ac100960f9f852d2161e895b9542b3e | `"linux"` | `"amd64"`    | `"bee3fd19a5e9de3bb2aa2e40de5592a9dba06a8c6653ec5c31831df51b5ec9ee"` | `"20.10.3"`   | `"407749778"` |
| https://w3id.org/docker/image/id/sha256%3A98e2db9506ab2563363d9d57f0206ef55c7a538c54aa966fc9a531e4a15dbeca | `"linux"` | `"amd64"`    | `"7ab0761589deff772b32664f90893ffaa6aa4f5e8d9b07000603749b1545827d"` | `"20.10.7"`   | `"423871271"` |
| https://w3id.org/docker/image/id/sha256%3Aba3d64554654107b5eeff2d0600acf6e03ca0fe5723fcdbab8d244a097d81bf9 | `"linux"` | `"amd64"`    | `"f1ef6dd017021c5f48c48e83d263bac7f01caaef4b640f2e761e1e70a084037b"` | `"20.10.3"`   | `"448257330"` |

```bash

```