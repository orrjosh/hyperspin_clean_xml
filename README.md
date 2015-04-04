# Hyperspin XML Cleanup
## Remove Missing Games

1. Create a missing games list from hyperspin for a particular console.

2. Copy the console game configuration from the same console into a temp directory along with the missing game list
 
3. Run the command

        remove_missing_games.py -i <inputfile> -o <outputfile> -m <missinggamelist>

4. Copy the output xml over the console game configuration file
