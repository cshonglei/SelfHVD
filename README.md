<div align="center">

# SelfHVD: Self-Supervised Handheld Video Deblurring

CVPR 2026

[Honglei Xu](mailto:cshongleixu@gmail.com) · [Zhilu Zhang](mailto:cszlzhang@outlook.com) · [Junjie Fan](mailto:zhou93108@gmail.com) · [Xiaohe Wu](mailto:csxhwu@gmail.com) · [Wangmeng Zuo](mailto:wmzuo@hit.edu.cn)

Harbin Institute of Technology

[![arXiv](https://img.shields.io/badge/arXiv-2508.08605-b31b1b.svg)](https://arxiv.org/abs/2508.08605)
[![Paper](https://img.shields.io/badge/Paper-PDF-blue.svg)](https://arxiv.org/pdf/2508.08605.pdf)
[![Project Page](https://img.shields.io/badge/Project-Page-green.svg)](https://cshonglei.github.io/SelfHVD/)

</div>

---

## 📝 Abstract

Shooting video with handheld shooting devices often results in blurry frames due to shaking hands and other instability factors. Although previous video deblurring methods have achieved impressive progress, they still struggle to perform satisfactorily on real-world handheld video due to the blur domain gap between training and testing data. To address the issue, we propose a self-supervised method for handheld video deblurring, which is driven by sharp clues in the video. First, to train the deblurring model, we extract the sharp clues from the video and take them as misalignment labels of neighboring blurry frames. Second, to improve the deblurring ability of the model, we propose a novel Self-Enhanced Video Deblurring (SEVD) method to create higher-quality paired video data. Third, we propose a Self-Constrained Spatial Consistency Maintenance (SCSCM) method to regularize the model, preventing position shifts between the output and input frames. Moreover, we construct synthetic and real-world handheld video datasets for handheld video deblurring. Extensive experiments on these and other common real-world datasets demonstrate that our method significantly outperforms existing self-supervised ones.

---

## 🔍 Overview

![Pipeline](https://github.com/cshonglei/SelfHVD/blob/main/images/pipeline.png?raw=true)

---

## 🎬 Visualization

<div align="center">

*Left: Blurry Input &nbsp;·&nbsp; Right: SelfHVD Output*

**GoProShake**

<img src="https://github.com/cshonglei/SelfHVD/blob/main/images/Visualization/rank002_006_start0039_score953_h264.gif?raw=true" width="100%"/>
<img src="https://github.com/cshonglei/SelfHVD/blob/main/images/Visualization/rank006_008_start0030_score379_h264.gif?raw=true" width="100%"/>
<img src="https://github.com/cshonglei/SelfHVD/blob/main/images/Visualization/rank016_002_start0000_score19_h264.gif?raw=true" width="100%"/>

<br>

**HVD**

<img src="https://github.com/cshonglei/SelfHVD/blob/main/images/Visualization/002_side_by_side.gif?raw=true" width="100%"/>
<img src="https://github.com/cshonglei/SelfHVD/blob/main/images/Visualization/004_side_by_side.gif?raw=true" width="100%"/>
<img src="https://github.com/cshonglei/SelfHVD/blob/main/images/Visualization/008_side_by_side.gif?raw=true" width="100%"/>

</div>

---

## 🗂️ Datasets

We introduce two new datasets for handheld video deblurring:

### GoProShake (Synthetic)

![GoProShake](https://github.com/cshonglei/SelfHVD/blob/main/images/A.png?raw=true)

### HVD (Real-World)

![HVD](https://github.com/cshonglei/SelfHVD/blob/main/images/B.png?raw=true)

---

## 🏋️ Training

Code and pre-trained models are coming soon.

---

## 📖 Citation

If you find this work useful, please cite our paper:

```bibtex
@inproceedings{xu2026selfhvd,
  title={SelfHVD: Self-Supervised Handheld Video Deblurring},
  author={Xu, Honglei and Zhang, Zhilu and Fan, Junjie and Wu, Xiaohe and Zuo, Wangmeng},
  booktitle={CVPR},
  year={2026}
}
```
