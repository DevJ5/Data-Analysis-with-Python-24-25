#!/usr/bin/env python3
#!/usr/bin/env python3


def file_extensions(filename):
    filenames_no_extension = []
    filenames_and_extensions = {}

    with open(filename, "r") as in_file:
        for line in in_file:
            line = line.strip()
            if len(line) == 0:
                continue
            elif "." not in line:
                filenames_no_extension.append(line)
            else:
                extension = line.split(".")[-1]
                try:
                    filenames_and_extensions[extension].append(line)
                except:
                    filenames_and_extensions[extension] = [line]

    return (filenames_no_extension, filenames_and_extensions)


def main():
    filenames_no_extension, filenames_and_extensions = file_extensions(
        "src/filenames.txt"
    )
    print(f"{len(filenames_no_extension)} files with no extension")
    for k, v in filenames_and_extensions.items():
        print(f"{k} {len(v)}")


if __name__ == "__main__":
    main()
