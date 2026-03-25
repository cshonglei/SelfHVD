# SelfHVD: Self-Supervised Handheld Video Deblurring (CVPR 2026)

[![arXiv](https://img.shields.io/badge/arXiv-2508.08605-b31b1b.svg)](https://arxiv.org/abs/2508.08605)
[![Project Page](https://img.shields.io/badge/Project-Page-green.svg)](https://cshonglei.github.io/SelfHVD/)

---

## 🗒️ TODO

- [ ] Release code
- [ ] Release pre-trained models
- [ ] Release GoProShake dataset
- [ ] Release HVD dataset

---

## 📝 Abstract

Shooting video with handheld shooting devices often results in blurry frames due to shaking hands and other instability factors. Although previous video deblurring methods have achieved impressive progress, they still struggle to perform satisfactorily on real-world handheld video due to the blur domain gap between training and testing data. To address the issue, we propose a self-supervised method for handheld video deblurring, which is driven by sharp clues in the video. First, to train the deblurring model, we extract the sharp clues from the video and take them as misalignment labels of neighboring blurry frames. Second, to improve the deblurring ability of the model, we propose a novel Self-Enhanced Video Deblurring (SEVD) method to create higher-quality paired video data. Third, we propose a Self-Constrained Spatial Consistency Maintenance (SCSCM) method to regularize the model, preventing position shifts between the output and input frames. Moreover, we construct synthetic and real-world handheld video datasets for handheld video deblurring. Extensive experiments on these and other common real-world datasets demonstrate that our method significantly outperforms existing self-supervised ones.

---

## 🔍 Overview

![Pipeline](https://github.com/cshonglei/SelfHVD/blob/main/images/pipeline.png?raw=true)

---

<!--
## 🎬 Visualization

<div align="center">

<h3>GoProShake</h3>

<img src="https://raw.githubusercontent.com/cshonglei/SelfHVD/main/images/compare_labels.png" width="100%"/>

<img src="https://github.com/cshonglei/SelfHVD/blob/main/images/Visualization/rank002_006_start0039_score953_h264.gif?raw=true" width="100%"/>
<img src="https://github.com/cshonglei/SelfHVD/blob/main/images/Visualization/rank006_008_start0030_score379_h264.gif?raw=true" width="100%"/>
<img src="https://github.com/cshonglei/SelfHVD/blob/main/images/Visualization/rank016_002_start0000_score19_h264.gif?raw=true" width="100%"/>

<br>

<h3>HVD</h3>

<img src="https://raw.githubusercontent.com/cshonglei/SelfHVD/main/images/compare_labels.png" width="100%"/>

<img src="https://github.com/cshonglei/SelfHVD/blob/main/images/Visualization/002_side_by_side.gif?raw=true" width="100%"/>
<img src="https://github.com/cshonglei/SelfHVD/blob/main/images/Visualization/004_side_by_side.gif?raw=true" width="100%"/>
<img src="https://github.com/cshonglei/SelfHVD/blob/main/images/Visualization/008_side_by_side.gif?raw=true" width="100%"/>

</div>

---
-->

## 🗄️ Datasets

### GoProShake (Synthetic) &nbsp; [[Download (Google Drive)](https://drive.google.com)]

<div align="center">

![GoProShake](https://github.com/cshonglei/SelfHVD/blob/main/images/A.png?raw=true)

</div>

GoProShake takes into account the OIS technology on handheld video capture, synthesizing blurry videos (red boxes) that contain sharp frames (green boxes). The top and bottom rows are training and test videos, respectively.

### HVD (Real-World) &nbsp; [[Download (Google Drive)](https://drive.google.com)]

<div align="center">

![HVD](https://github.com/cshonglei/SelfHVD/blob/main/images/B.png?raw=true)

</div>

HVD is a real-world handheld video dataset. Sharp frames (green boxes) are present and reliable in most handheld shooting scenarios.

---

## 🏋️ Training

Code and pre-trained models are coming soon.

---

## 📖 Citation

```bibtex
@inproceedings{xu2026selfhvd,
  title={SelfHVD: Self-Supervised Handheld Video Deblurring},
  author={Xu, Honglei and Zhang, Zhilu and Fan, Junjie and Wu, Xiaohe and Zuo, Wangmeng},
  booktitle={CVPR},
  year={2026}
}
```
