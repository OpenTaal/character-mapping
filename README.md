# character-mapping

Users searching for words need to enter what they are searching for by either typing on a keyboard or by doing a copy-paste action. Providing a word in this way for search purposes is error prone on a character level for several reasons. A user might inadvertently use a wrong character, a user might use a character suiting typographic needs or software, such as a word processor or operating system, might have automatically alter a character.

Automated mapping or characters is in some cases justified to suggest a user what he or she might be actually searching for. Some examples will now follow illustrating often seen problems and solutions for the Dutch language.

A user might enter an ij-ligature `ĳ`, Unicode character 'LATIN SMALL LIGATURE IJ' (U+0133), when search for a word such as `zijn`. Support for this ligarature, which used to be widely available on many typewriters, arrived relatively late on computers. Hence the convention at the moment is that one has to enter two separate characters, an `i` followed by a `j`, resulting in "ij". Literally searching for the the ij-ligature `ĳ` will usually not give any results unless this characters is mapped on the pair of characters `i` and `j`.

In this case, searching for `zĳn` (three characters) will need to be mapped onto `zijn` (four characters). Note that using an ij-ligature is not incorrect, especially when chosen for typographic purposes. A similar example could be given for English regarding `ﬁ` for the fi-ligature. However, that ligature is used only for typographic purposes while `ĳ` is an actual character in (hand)written form of Dutch. In the context of this project, these kind of mappings are called a REPLACE.

Another case is the Dutch word `'s ochtends` which starts with an apostrophe in handwriting. Here too a convention exits, which is to use the single quote `'` and not the Unicode Character 'RIGHT SINGLE QUOTATION MARK' (U+2019) `’`. This also needs a REPLACE mapping, but it gets worse. Some operating systems or word processors automatically replace the single quote `'` with an `‘`, Unicode Character 'LEFT SINGLE QUOTATION MARK' (U+2018) because software has (incorrectly) determined that the writer is starting a quotation. For this reason both `’` and `‘` need to be replaced by `'`.

A third example would be the use of a soft hypen, Unicode Character 'SOFT HYPHEN' (U+00AD). Normally, the soft hyphen is invisible for the user. This character will only appear as `-` when hyphenation of a word takes is at the location of a soft hyphen character. This can be a very practical character but needs to be removed from the user input when plain text searches are done. In the context of this project, a mapping removing unwanted characters is called a DELETE.

The non-breaking space, Unicode Character 'NO-BREAK SPACE' (U+00A0), is a character with a similar functional origin. Dutch words such as "te allen tijde" contain one or more spaces. But when this space is replaced by another spacing character, exact matching is not possible. Therefore replacing alternative spacing it with a normal space character is justifiable for searching purposes.

Sloppy typing or formatting can introduce multiple spaces where one space would suffice. Suppose "ad hoc" is written as "ad  hoc" with two spaces, then reducing all additional spaces until only one is left is desired. This kind of mapping is called REDUCE in the context of this project.

Another form of deletion would be needed for superfluous characters such as "®" and "™" but also for any keyboard character found on QWERTY, AZERTY and QWERTZ keyboards that might have been entered accidentally e.g. `¨` or have hitched along on a copy-paste action. Additionally, more exotic characters can be constructed by means of a compose key or dead key such as `ß` or `č` require some form of mapping as well.

TODO: what has been created

Characters not included are:
- characters which represent different characters in encoding problems such as þ in huidcrþme (huidcrème), blþren (blèren) and faþade (façade).
- ligature characters which are rarely used, such as historical ligatures ᵫ (ue), ʤ (dz) and Ꜽ (AY).
- characters with diacritics which are rarely used, such as `ǰ` → `j`. However, this varies per character as `č` → `c` is supported.

Out of scope here is:
- casting between uppercase and lowercase and vice verse, see https://github.com/OpenTaal/case-casting
- removal of diacritics on characters, https://github.com/OpenTaal/diacritic-removal
- fixing character encoding errors such as Ã¼ en â€ž, see http://www.i18nqa.com/debug/utf8-debug.html
- fixing url encoding errors such as %20, see http://www.w3schools.com/tags/ref_urlencode.asp
- removal of HTML or XML elements such as &amp; and &nbsp;, see http://www.ascii.cl/htmlcodes.htm
