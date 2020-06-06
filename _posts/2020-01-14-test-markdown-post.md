---
toc: true
layout: post
description: fastpages实现markdown文章示例
categories: [markdown]

title: Markdown文章示例
---

# Markdown文章示例

## 基本设置

Jekyll要求文件名称进行如下配置：

`YEAR-MONTH-DAY-filename.md`

其中`YEAR`是4位年份(2020)，`MONTH`(06) 和 `DAY`(04) 都是两位数字，`filename`文件名随便取，方便查询即可。`.md` 是markdown文件后缀。

文件正文第一行标题需要用`#`开始，后面跟空格，在增加标题内容。这样就实现了markdown的*一级标题*。然后也可以用多个`#`创建2、3级等标题，例如上面的二级标题`## 基本设置`。


## 基本样式

可以实现 *斜体*, **加粗**, `代码字体`，还有[链接](https://www.markdownguide.org/cheat-sheet/)，以及尾注[^1]和水平线：

---

## 列表

一个列表

- item 1
- item 2

带序号列表

1. item 1
1. item 2

## 提示文字（Boxes and stuff）

> 这是提示文字

{% include alert.html text="You can include alert boxes" %}

...以及...

{% include info.html text="You can include info boxes" %}

## 图像

![]({{ site.baseurl }}/images/logo.png "fast.ai's logo")

## 代码

可以配置文字和代码格式

一般文字：

    # Do a thing
    do_thing()

Python代码和输出：

```python
# Prints '2'
print(1+1)
```

    2

shell命令格式：

```shell
echo "hello world"
./some_script.sh --option "value"
wget https://example.com/cat_photo1.png
```

YAML格式：

```yaml
key: value
- another_key: "another value"
```


## 表格

| Column 1 | Column 2 |
|-|-|
| A thing | Another thing |


## Tweet卡片

{% twitter https://twitter.com/jakevdp/status/1204765621767901185?s=20 %}


## 尾注



[^1]: This is the footnote.

