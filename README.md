# Natural language processing course 2022/23: `Project 3: Paraphrasing sentences`

Team members:
 * `DREJC PESJAK`, `63180224`, `dp8949@student.uni-lj.si`
 * `KLEMEN VOVK`, `63190317`, `kv4582@student.uni-lj.si`
 * `ILIJA TAVCHIOSKI`, `63180383`, `it8816@student.uni-lj.si`
 
Group public acronym/name: `DS-elita`

## Data
The translated dataset is a subset of the [ParaBank2](https://nlp.jhu.edu/parabank/) dataset (first 100.000 rows) and can be downloaded [here](https://unilj-my.sharepoint.com/:u:/g/personal/kv4582_student_uni-lj_si/Efaka4o7MGJOilz7colF34EB039AxbwfpCtDRaJx_DoCKg?e=JC9vSB).

Dataset processing code can be found in src/translations. Translations were done with the Slovene NMT model available [here](https://github.com/clarinsi/Slovene_NMT).


## Fine-tuning the sloGPT model
We used the pretrained large language model [GPT-sl-base](https://huggingface.co/cjvt/gpt-sl-base) and finetuned it on the dataset generated above. The finetuned model is available [here](https://drive.google.com/file/d/1fsC-qPfzYh72CzVPifpoBJGbS8XrbCC_/view?usp=sharing). The finetuning code can be found in finetune-slo-paraphrase-gpt.ipynb.
The model was finetuned for 3 epochs with a batch size of 16 and a learning rate of 5e-5. The model was trained on Kaggle, on a double Tesla T4 GPU with 16GB of memory. The training took about 12 hours, before capping out due to Kaggle limitations. During that time it did 70k steps, which is 1.23 epochs, where the training loss dropped from 0.36 to 0.076.

The finetuned model evaluated with the BLEU score. The data can be found in [here](https://drive.google.com/file/d/1_coX9bRgna9gts4GzGsEs1YTB2D7AEh_/view?usp=sharing). The evaluation code can be found in the src/slopara-gpt-testing.ipynb notebook.
