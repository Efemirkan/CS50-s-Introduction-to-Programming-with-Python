import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):

    # Check for the first pattern of YouTube iframe tag
    if matches := re.search(r'^<iframe src="(https?://(?:www\.)?youtube\.com/embed/\w+?)"></iframe>$', s, re.IGNORECASE):

        # Extract the URL from the first pattern
        url = matches.group(1)

        # Replace the URL format with "https://youtu.be/"
        url1 = re.sub(r"https?://(?:www\.)?youtube\.com/embed/", "https://youtu.be/", url)

        # Return the modified URL
        return url1

    # Check for the first pattern of YouTube iframe tag
    if matches := re.search(r'^<iframe width="560" height="315" src="(https?://(?:www\.)?youtube\.com/embed/\w+?)" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>$', s, re.IGNORECASE):

        # Extract the URL from the first pattern
        url = matches.group(1)

        # Replace the URL format with "https://youtu.be/"
        url1 = re.sub(r"https?://(?:www\.)?youtube\.com/embed/", "https://youtu.be/", url)

        # Return the modified URL
        return url1

if __name__ == "__main__":
    main()
