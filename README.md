# SelfHVD: Self-Supervised Handheld Video Deblurring (CVPR 2026)

[![arXiv](https://img.shields.io/badge/arXiv-2508.08605-b31b1b.svg)](https://arxiv.org/abs/2508.08605)
[![Project Page](https://img.shields.io/badge/Project-Page-green.svg)](https://cshonglei.github.io/SelfHVD/)

---

## 📝 Abstract

Shooting video with handheld shooting devices often results in blurry frames due to shaking hands and other instability factors. Although previous video deblurring methods have achieved impressive progress, they still struggle to perform satisfactorily on real-world handheld video due to the blur domain gap between training and testing data. To address the issue, we propose a self-supervised method for handheld video deblurring, which is driven by sharp clues in the video. First, to train the deblurring model, we extract the sharp clues from the video and take them as misalignment labels of neighboring blurry frames. Second, to improve the deblurring ability of the model, we propose a novel Self-Enhanced Video Deblurring (SEVD) method to create higher-quality paired video data. Third, we propose a Self-Constrained Spatial Consistency Maintenance (SCSCM) method to regularize the model, preventing position shifts between the output and input frames. Moreover, we construct synthetic and real-world handheld video datasets for handheld video deblurring. Extensive experiments on these and other common real-world datasets demonstrate that our method significantly outperforms existing self-supervised ones.

---

## 🔍 Overview

![Pipeline](https://github.com/cshonglei/SelfHVD/blob/main/images/pipeline.png?raw=true)

Overview of our SelfHVD. Given a blurry video captured by a handheld shooting device, we first select the sharp frames and take them as misalignment labels. Then, Self-Enhanced Video Deblurring (SEVD) constructs higher-quality paired training data to further improve the model performance. Self-Constrained Spatial Consistency Maintenance (SCSCM) is proposed to prevent position shifts between output and input frames.

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

<a name="datasets"></a>

## 🗄️ Datasets

<div align="center">

### [GoProShake](https://github.com/cshonglei/SelfHVD)

![GoProShake](https://github.com/cshonglei/SelfHVD/blob/main/images/A.png?raw=true)

</div>

Visualization of GoProShake dataset. The top and bottom are training and test videos, respectively. GoProShake takes into account the OIS technology on handheld video capture, synthesizing blurry videos (red boxes) that contain sharp frames (green boxes).

<div align="center">

### [HVD](https://github.com/cshonglei/SelfHVD)

![HVD](https://github.com/cshonglei/SelfHVD/blob/main/images/B.png?raw=true)

</div>

Visualization of HVD dataset. Sharp frames (green boxes) are present and reliable in most cases of handheld shooting scenarios.

---

## 🚀 Quick Start

### 1. Installation

Prepare an environment with **PyTorch** from [pytorch.org](https://pytorch.org/). If you are experienced with PyTorch and have already installed it, just skip this part and jump to the next section.

<pre style="overflow-x: auto; max-width: 100%; white-space: pre;"><code class="language-bash">conda create --name selfhvd python=3.8 -y
conda activate selfhvd
conda install pytorch torchvision cudatoolkit=11.3 -c pytorch</code></pre>

Install **MMCV-full** (must match your PyTorch and CUDA). Using [OpenMIM](https://github.com/open-mmlab/mim) is recommended.

   ```bash
   pip install -U openmim
   mim install mmcv-full
   ```

Clone repository and install it.

   ```bash
   git clone https://github.com/cshonglei/SelfHVD.git
   cd SelfHVD
   pip install -v -e .
   ```

### 2. Prepare Data

Put `.mp4` files under `data/`, then run:

```bash
python data/videos2images.py
```

Then `data/test_videos/` has a folder with the same name as each video. All frames from that video are saved in that folder as `00000000.png`, `00000001.png`, …; for example, `000.mp4` is unpacked to `data/test_videos/000/`.

```text
data/test_videos/
  └── 000/
        00000000.png
        00000001.png
        ...
```

### 3. Run Inference

Download the pretrained checkpoint from [Google Drive](https://drive.google.com/file/d/1UWxS8MPrd5gpret_o-wz1vVjIcSciIMs/view?usp=drive_link). Save the file under this repository as `chkpts/pretrain.pth`, then run:

<pre style="overflow-x: auto; max-width: 100%; white-space: pre;"><code class="language-bash">python tools/test.py configs/basicvsr_plusplus_deblur.py chkpts/pretrain.pth --save-path demo/test_result</code></pre>

Restored frames are written under `demo/test_result/` by default. Change `--save-path` to any directory you want outputs saved under.

---

## 🏋️ Training

Coming soon.

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
