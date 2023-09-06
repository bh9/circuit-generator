# circuit-generator
The tool I use to generate WOD style circuits for my classes

To generate a random list of exercises:
`jq '.[] | .name' exercises | shuf -n<number>`

To generate a random list of exercises in a group:
`jq '.[] | select(.groups[] | contains ("<group>")) | .name' exercises | shuf -n<number>`
