# SelfHVD: Self-Supervised Handheld Video Deblurring for Mobile Phones

## 🧾 Abstract

Shooting video with a handheld mobile phone, the most common photographic device, often results in blurry frames due to shaking hands and other instability factors. Although previous video deblurring methods have achieved impressive progress, they still struggle to perform satisfactorily on real-world handheld video due to the blur domain gap between training and testing data. To address the issue, we propose a self-supervised method for handheld video deblurring, which is driven by sharp clues in the video. First, to train the deblurring model, we extract the sharp clues from the video and take them as misalignment labels of neighboring blurry frames. Second, to improve the model's ability, we propose a novel Self-Enhanced Video Deblurring (SEVD) method to create higher-quality paired video data. Third, we propose a Self-Constrained Spatial Consistency Maintenance (SCSCM) method to regularize the model, preventing position shifts between the output and input frames. Moreover, we construct a synthetic and a real-world handheld video dataset for handheld video deblurring. Extensive experiments on these two and other common real-world datasets demonstrate that our method significantly outperforms existing self-supervised ones. The code and datasets will be publicly available.

## 🏋️‍♂️ Training

Code is coming soon.

## 🧩 Pipeline

<img src="figs/pipeline.png" alt="SelfHVD Pipeline" width="800"/>

## 📄 Citation

If you find this work useful, please cite our paper:

```bibtex
@article{SelfHVD, 
    title  = {SelfHVD: Self-Supervised Handheld Video Deblurring for Mobile Phones}, 
    author = {Xu, Honglei and Zhang, Zhilu and Fan, Junjie and Wu, Xiaohe and Zuo, Wangmeng}, 
    year   = {2025}
}
