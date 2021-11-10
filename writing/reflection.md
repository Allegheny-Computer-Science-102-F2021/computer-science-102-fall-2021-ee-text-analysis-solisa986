# Text Analysis

## Adriana Solis

## Program Input and Output

### What is the output from running the following command?

`poetry run textanalysis --output-file text/generated_two.txt --generate`

```
C:\Users\solis\OneDrive\Documents\cs102F2021\labs\computer-science-102-fall-2021-ee-text-analysis-solisa986\textanalysis>poetry run textanalysis --output-file text/generated_two.txt --generate
✨ Generating text for subsequent analysis!
Downloading: 100%|████████████████████████████████████████████████████████████████████████████| 665/665 [00:00<?, ?B/s]
Downloading: 100%|██████████████████████████████████████████████████████████████████| 523M/523M [07:40<00:00, 1.19MB/s]

🖌  Here is the automatically generated text:

A study by the University of California, Berkeley's Center for Applied Environmental Studies (CEEAS), has found that the
use of "fungicide" or "toxic chemical" for human use is a growing problem for the planet.

The study, published in the journal Environmental Science & Technology, shows that more than 1 in 5 people in the United
States and Canada, and more than 1 in 10 people in Europe, are exposed to chemical herbicides and herbicides as a result
of exposure to certain chemicals.

It's not much of a stretch to say that there are very few ways to prevent human exposure to chemical herbicides and
herbicides. The vast majority of the chemicals used in the world are used at the highest levels, and most are either
used with or without human intervention. Yet, that's where our "fungicide" problem becomes more problematic.

"In the last 10 years or so, about half of all the global chemical herbicides and herbicides used in the world have
resulted in human-caused impacts," says co-author Richard L. Muhlberg, director of the UCSB Center for Applied
Environmental Studies.

In 2010, for instance, the U.S. Environmental Protection Agency released a
```

### What is the output from running the following command?

`poetry run textanalysis --input-file text/input_one.txt --analyze`

```
C:\Users\solis\OneDrive\Documents\cs102F2021\labs\computer-science-102-fall-2021-ee-text-analysis-solisa986\textanalysis>poetry run textanalysis --input-file text/input_one.txt --analyze
✨ Let's characterize the file and its words!

        The input file contains 23 lines, including blank lines!
        The input file contains 19 lines, not including blank lines!
        The input file contains 5 paragraphs!
        The input file contains 118 unique words across all sets!
        The words that are found across all sets are: {'Make', 'to'}

🖌  Saving the visualization in graphics/set-visualization.png

🔬 Get ready, here is the analysis of the sets!

{
    frozenset({0}): {
        'without',
        'recorded',
        'supply',
        'end',
        'are',
        'because',
        'build',
        'these',
        'user',
        'install',
        'details',
        'enables',
        'done',
        'knowing'
    },
    frozenset({0, 2}): {'your', 'of', 'and', 'that'},
    frozenset({3}): {
        'documentation',
        'particular',
        'compiler',
        'an',
        'object',
        'linker',
        'library',
        'commands',
        'For',
        'format',
        'each',
        'TeX',
        'language',
        'produce',
        'These',
        'executable',
        'compute',
        'any',
        'specifies',
        'shell',
        'Makeinfo',
        'ar'
    },
    frozenset({2}): {
        'only',
        'all',
        'few',
        'result',
        'recompile',
        'does',
        'updates',
        'directly',
        'change',
        'indirectly',
        'need',
        'depend',
        'those',
        'if',
        'As',
        'then'
    },
    frozenset({4}): {
        'enough',
        'while',
        'do',
        'else',
        'building',
        'anything',
        'worth',
        'installing',
        'make',
        'control',
        'writing',
        'down',
        'often',
        'tags',
        'tables',
        'generate',
        'use',
        'You',
        'want',
        'deinstalling'
    },
    frozenset({0, 4}): {'how', 'package'},
    frozenset({0, 1, 2, 3, 4}): {'Make', 'to'},
    frozenset({1, 2}): {'It', 'files', 'on', 'changed'},
    frozenset({1, 2, 3}): {'source', 'non'},
    frozenset({1}): {
        'case',
        'another',
        'needs',
        'out',
        'depends',
        'figures',
        'updating',
        'have',
        'order',
        'one',
        'which',
        'automatically',
        'proper',
        'based',
        'determines'
    },
    frozenset({2, 3, 4}): {'or', 'a', 'not'},
    frozenset({0, 3, 4}): {'is'},
    frozenset({3, 4}): {'can', 'limited'},
    frozenset({1, 4}): {'also', 'for'},
    frozenset({0, 3}): {'makefile'},
    frozenset({0, 1, 2, 3}): {'the'},
    frozenset({1, 3}): {'update', 'file'},
    frozenset({2, 3}): {'program', 'run'},
    frozenset({0, 2, 4}): {'you'},
    frozenset({1, 2, 3, 4}): {'it'},
    frozenset({0, 1, 3}): {'in'}
}
```

### What is the output from running the following command?

`poetry run textanalysis --input-file text/generated_one.txt --analyze`

```
C:\Users\solis\OneDrive\Documents\cs102F2021\labs\computer-science-102-fall-2021-ee-text-analysis-solisa986\textanalysis>poetry run textanalysis --input-file text/generated_one.txt --analyze
✨ Let's characterize the file and its words!

        The input file contains 15 lines, including blank lines!
        The input file contains 8 lines, not including blank lines!
        The input file contains 8 paragraphs!
        The input file contains 110 unique words across all sets!
        The words that are found across all sets are: None

🖌  Saving the visualization in graphics/set-visualization.png

🔬 Get ready, here is the analysis of the sets!

{
    frozenset({5}): {'didn', 'last', 'then', '1', 'long', 'October', 'which'},
    frozenset({1}): {
        'private',
        'March',
        'carried',
        'contained',
        'bottle',
        'it',
        'from',
        'claimed',
        'out',
        'called',
        'and',
        'Oceans'
    },
    frozenset({7}): {'talking', 'about', 'no', 'Unfortunately', 'tell', 'means', 'way', 'is'},
    frozenset({0}): {
        'related',
        'did',
        'Ryan',
        'been',
        's',
        'someone',
        'position',
        'would',
        'incident',
        'lead',
        'scandal',
        'have',
        'hard',
        'believe',
        'like',
        'take',
        'such',
        'kind',
        'serious',
        'this'
    },
    frozenset({2}): {
        'help',
        'my',
        'photo',
        'told',
        'According',
        'feel',
        'I',
        'couldn',
        'June',
        'Guardian',
        '27',
        'miracle',
        'what',
        'reported',
        'never',
        'but',
        'God',
        'Oh',
        'issue',
        '2016',
        'health',
        'taken'
    },
    frozenset({6}): {'nearly', 'two', 'took', 'years'},
    frozenset({4, 5}): {'2017'},
    frozenset({0, 2, 3, 7}): {'that'},
    frozenset({1, 3}): {'photograph', 'with'},
    frozenset({0, 1}): {'in', 'of', 'water'},
    frozenset({0, 1, 2, 3, 5}): {'a'},
    frozenset({3}): {'authentic', 'But', 'ruled', 'court', 'problem'},
    frozenset({0, 1, 2, 3, 5, 6, 7}): {'the'},
    frozenset({3, 5}): {'filed', 'defamation', 'against'},
    frozenset({0, 3}): {'not'},
    frozenset({0, 1, 2, 6, 7}): {'to'},
    frozenset({1, 2, 3, 4, 5}): {'was', 'The'},
    frozenset({4}): {'September', '25th'},
    frozenset({3, 5, 6}): {'for'},
    frozenset({2, 3}): {'had'},
    frozenset({0, 7}): {'who'},
    frozenset({0, 1, 2, 5, 6}): {'It'},
    frozenset({4, 5, 6}): {'dismissed'},
    frozenset({1, 2, 4, 5}): {'on'},
    frozenset({0, 1, 2, 3, 5, 7}): {'Lochte'},
    frozenset({1, 3, 5}): {'family'},
    frozenset({3, 4, 5, 6}): {'lawsuit'},
    frozenset({1, 2, 3, 5}): {'website'},
    frozenset({1, 7}): {'hoax'},
    frozenset({2, 5}): {'t'},
    frozenset({3, 7}): {'there'},
    frozenset({1, 6}): {'be'}
}
```

### What is inside of the `generated_two.txt` file that your tool created?

```
A study by the University of California, Berkeley's Center for Applied Environmental Studies (CEEAS), has found that the use of "fungicide" or "toxic chemical" for human use is a growing problem for the planet.

The study, published in the journal Environmental Science & Technology, shows that more than 1 in 5 people in the United States and Canada, and more than 1 in 10 people in Europe, are exposed to chemical herbicides and herbicides as a result of exposure to certain chemicals.

It's not much of a stretch to say that there are very few ways to prevent human exposure to chemical herbicides and herbicides. The vast majority of the chemicals used in the world are used at the highest levels, and most are either used with or without human intervention. Yet, that's where our "fungicide" problem becomes more problematic.

"In the last 10 years or so, about half of all the global chemical herbicides and herbicides used in the world have resulted in human-caused impacts," says co-author Richard L. Muhlberg, director of the UCSB Center for Applied Environmental Studies.

In 2010, for instance, the U.S. Environmental Protection Agency released a
```

### What is inside of the `input_two.txt` file that you downloaded and saved?

```
Under a spreading chestnut-tree
The village smithy stands;
The smith, a mighty man is he,
With large and sinewy hands,
And the muscles of his brawny arms
Are strong as iron bands.

His hair is crisp, and black, and long;
His face is like the tan;
His brow is wet with honest sweat,
He earns whate'er he can,
And looks the whole world in the face,
For he owes not any man.

Week in, week out, from morn till night,
You can hear his bellows blow;
You can hear him swing his heavy sledge,
With measured beat and slow,
Like a sexton ringing the village bell,
When the evening sun is low.

And children coming home from school
Look in at the open door;
They love to see the flaming forge,
And hear the bellows roar,
And catch the burning sparks that fly
Like chaff from a threshing-floor.

He goes on Sunday to the church,
And sits among his boys;
He hears the parson pray and preach,
He hears his daughter's voice
Singing in the village choir,
And it makes his heart rejoice.

It sounds to him like her mother's voice,
Singing in Paradise!
He needs must think of her once more,
How in the grave she lies;
And with his hard, rough hand he wipes
A tear out of his eyes.

Toiling,—rejoicing,—sorrowing,
Onward through life he goes;
Each morning sees some task begin,
Each evening sees it close;
Something attempted, something done,
Has earned a night's repose.

Thanks, thanks to thee, my worthy friend,
For the lesson thou hast taught!
Thus at the flaming forge of life
Our fortunes must be wrought;
Thus on its sounding anvil shaped
Each burning deed and thought.
```

## Source Code

### Describe in detail how your provided source code works

#### Please explain each line of source code from the `extract` module

Write at least one paragraph to explain the requested source code

```python
def extract_paragraphs(input_lines: str) -> List[str]:
    """Extract all of the paragraphs from the lines of textual input."""
    # Reference:
    # https://stackoverflow.com/questions/53240763/python-how-to-separate-paragraphs-from-text
    no_newlines = input_lines.strip("\n")
    split_text = NEWLINES_RE.split(no_newlines)
    paragraphs = [p + "\n" for p in split_text if p.strip()]
    return paragraphs
```

This defined function first intializes a variable 'input_lines' with a type string. Through type annotation, we see that the program is expected to return a list of strings. In the first section of code, the declared string will be stripped and removed of leading a trailing new line characters. The next line will be where the text is split in the case of if there are two or more newline characters, such as the beginning and ending of a paragraph. The next part features list comprehension, which is when more than one operation is performed within a list declaration. The first operation of 'p + "\n"' ensures that all lines in the paragraph ends with a new line. The second operation iterates through the split text, where 'p.strip()' is evaluated. If true, the paragraph has other characters other than whitespace. The function will return the simplified paragraphs, which are a list of strings that do not contain any new line characters or whitespace.

## Analyzing the Text

### According to the output of your program, what words does `input_one.txt` have in common across all paragraphs? How did you know?

The words that input_one.txt has in common across all of the paragraphs is 'Make' and 'to'. I know this because of the output of the program. This output is determined by analyzing the words inside of all of the sets generated for each paragraph. This is done using the union function, where all sets are combined together. Since a set deletes any duplicate values, then this generates a single set that contains only words that were in the text file once. In order to find the common words against all paragraphs, we would then intersect the set generated from the union function with all of the different sets. This will check to see which unique words are found inside each of the sets (ergo, which words are found inside all of the paragraphs). These words are then saved inside the set, where they will output the common unique words.

### Using the console output and visualization for the `input_one.txt`, what trends do you see? Interpret these trends.

In the console output, I noticed that there were a lot of words that were not found in any of the other sets. Most of the unique words came from Set  and Set 3, which contains the words from paragraph 3 and 4. The total number of words inside of each set are relatively the same, ranging from 27-40 words. 

### Using the console output and visualization for the `generated_one.txt`, what trends do you see? Interpret these trends.

Provide response to this question, demonstrating your knowledge of the use and visualization of sets.

## Professional Development

### What are the similarities and differences between `set`, `FrozenSet`, and `FiniteSet`?

Provide a response to this question, explaining these three implementations of the set discrete structure.

### At an intuitive and informal level what is the `aitextgen` package and how does it work?

Provide a response to this question, leveraging the documentation for this tool on sites like GitHub.

### At your own option, do you have any other insights to share about this assignment?

At your own option, provide further insights about this assignment!
