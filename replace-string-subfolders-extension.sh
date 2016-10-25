# Replace a string in all files with a given extension
# $1 argument is the extension
# $2 argument is the string to replace
# $3 argument is the string to put instead of the $2 string
find . -type f -name "**."$1"" -exec sed -i '' 's/'"$2"'/'"$3"'/g' {} +
