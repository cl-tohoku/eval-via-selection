# Dialogue Response Selection Test Set with Well-Chosen False Candidates
## Statistics
Below are statistics for the test set:
- Total questions: 1,019
- Candidates per question: 4
- Context turns per question: 3

## Create the test dataset
### 1. Prepare the OpenSubtitles data
This dataset uses movie and television subtitles data from OpenSubtitles. See http://opus.nlpl.eu/OpenSubtitles-v2018.php and the following citation:

> P. Lison and J. Tiedemann, 2016, OpenSubtitles2016: Extracting Large Parallel Corpora from Movie and TV Subtitles. LREC 2016.

```
wget 'http://opus.nlpl.eu/download.php?f=OpenSubtitles/v2018/mono/OpenSubtitles.raw.en.gz' -O en.txt.gz
gunzip en.txt.gz
```

### 2. Prepare the DailyDialog data
This dataset uses multi-turn dialog data from OpenSubtitles. See http://yanran.li/dailydialog and the following citation:

> Yanran Li, Hui Su, Xiaoyu Shen, Wenjie Li, Ziqiang Cao, and Shuzi Niu. DailyDialog: A Manually Labelled Multi-turn Dialogue Dataset. IJCNLP 2017.

```
wget 'http://yanran.li/files/ijcnlp_dailydialog.zip' ijcnlp_dailydialog.zip
unzip ijcnlp_dailydialog.zip
```

### 3. Extract the utterances
```
bash create_test.sh en.txt ijcnlp_dailydialog/dialogues_text.txt [TestsetName]
``` 
