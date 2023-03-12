#!/bin/bash

# Get the latest tag
latestTag=$(git describe --tags `git rev-list --tags --max-count=1`)

# # Get the latest commit hash
# latestCommit=$(git rev-parse HEAD)

# # Get the latest commit hash with a tag
# taggedCommit=$(git rev-list -n 1 $latestTag)

# # Check if the latest commit has a tag
# if [ $latestCommit == $taggedCommit ]; then
#     echo "No new commits since last tag."
#     exit 0
# fi

echo $latestTag

# Split the tag into an array by dot
tagArray=(${latestTag//./ })

# Get the major, minor and patch numbers
major=${tagArray[0]}
minor=${tagArray[1]}
patch=${tagArray[2]}

# Check the commit message for #major or #minor
commitMessage=$(git log -1 --pretty=%B)
if [[ $commitMessage == *#major* ]]; then
    major=$((major + 1))
    minor=0
    patch=0
elif [[ $commitMessage == *#minor* ]]; then
    minor=$((minor + 1))
    patch=0
else
    patch=$((patch + 1))
fi

# Create the new tag
newTag="$major.$minor.$patch"
echo "New tag: $newTag"
git tag $newTag

# Replace the version in __init__.py with the new tag
sed -i "s/__version__ = .*/__version__ = \"$newTag\"/" versioning/__init__.py
