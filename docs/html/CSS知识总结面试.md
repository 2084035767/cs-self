# CSS知识总结面试

#### 1.介绍一下标准的 CSS 的盒子模型？低版本 IE 的盒子模型有什么不同的？

相关知识点：

```
（1）有两种盒子模型：IE盒模型（border-box）、W3C标准盒模型（content-box）
（2）盒模型：分为内容（content）、填充（padding）、边界（margin）、边框（border）四个部分

IE盒模型和W3C标准盒模型的区别：

（1）W3C标准盒模型：属性width，height只包含内容content，不包含border和padding
（2）IE盒模型：属性width，height包含content、border和padding，指的是content
+padding+border。

在ie8+浏览器中使用哪个盒模型可以由box-sizing（CSS新增的属性）控制，默认值为content-box，即标准盒模型；
如果将box-sizing设为border-box则用的是IE盒模型。如果在ie6，7，8中DOCTYPE缺失会将盒子模型解释为IE
盒子模型。若在页面中声明了DOCTYPE类型，所有的浏览器都会把盒模型解释为W3C盒模型。
```

回答：

```
盒模型都是由四个部分组成的，分别是margin、border、padding和content。

标准盒模型和IE盒模型的区别在于设置width和height时，所对应的范围不同。标准盒模型的width和height属性的
范围只包含了content，而IE盒模型的width和height属性的范围包含了border、padding和content。

一般来说，我们可以通过修改元素的box-sizing属性来改变元素的盒模型。
```

详细的资料可以参考：
[《CSS 盒模型详解》](https://juejin.im/post/59ef72f5f265da4320026f76)

#### 2.CSS 选择符有哪些？

```
（1）id选择器（#myid）
（2）类选择器（.myclassname）
（3）标签选择器（div,h1,p）
（4）后代选择器（h1 p）
（5）相邻后代选择器（子）选择器（ul>li）
（6）兄弟选择器（li~a）
（7）相邻兄弟选择器（li+a）
（8）属性选择器（a[rel="external"]）
（9）伪类选择器（a:hover,li:nth-child）
（10）伪元素选择器（::before、::after）
（11）通配符选择器（*）
```

#### 3.::before 和:after 中双冒号和单冒号有什么区别？解释一下这 2 个伪元素的作用。

相关知识点：

```
单冒号（:）用于CSS3伪类，双冒号（::）用于CSS3伪元素。（伪元素由双冒号和伪元素名称组成）
双冒号是在当前规范中引入的，用于区分伪类和伪元素。不过浏览器需要同时支持旧的已经存在的伪元素写法，
比如:first-line、:first-letter、:before、:after等，
而新的在CSS3中引入的伪元素则不允许再支持旧的单冒号的写法。

想让插入的内容出现在其它内容前，使用::before，否者，使用::after；
在代码顺序上，::after生成的内容也比::before生成的内容靠后。
如果按堆栈视角，::after生成的内容会在::before生成的内容之上。
```

回答：

```
在css3中使用单冒号来表示伪类，用双冒号来表示伪元素。但是为了兼容已有的伪元素的写法，在一些浏览器中也可以使用单冒号
来表示伪元素。

伪类一般匹配的是元素的一些特殊状态，如hover、link等，而伪元素一般匹配的特殊的位置，比如after、before等。
```

#### 4.伪类与伪元素的区别

```
css引入伪类和伪元素概念是为了格式化文档树以外的信息。也就是说，伪类和伪元素是用来修饰不在文档树中的部分，比如，一句
话中的第一个字母，或者是列表中的第一个元素。

伪类用于当已有的元素处于某个状态时，为其添加对应的样式，这个状态是根据用户行为而动态变化的。比如说，当用户悬停在指定的
元素时，我们可以通过:hover来描述这个元素的状态。

伪元素用于创建一些不在文档树中的元素，并为其添加样式。它们允许我们为元素的某些部分设置样式。比如说，我们可以通过::be
fore来在一个元素前增加一些文本，并为这些文本添加样式。虽然用户可以看到这些文本，但是这些文本实际上不在文档树中。

有时你会发现伪元素使用了两个冒号（::）而不是一个冒号（:）。这是CSS3的一部分，并尝试区分伪类和伪元素。大多数浏览
器都支持这两个值。按照规则应该使用（::）而不是（:），从而区分伪类和伪元素。但是，由于在旧版本的W3C规范并未对此进行
特别区分，因此目前绝大多数的浏览器都支持使用这两种方式表示伪元素。
```

详细资料可以参考：
[《总结伪类与伪元素》](http://www.alloyteam.com/2016/05/summary-of-pseudo-classes-and-pseudo-elements/)

#### 5.CSS 中哪些属性可以继承？

相关资料：

```
每个CSS属性定义的概述都指出了这个属性是默认继承的，还是默认不继承的。这决定了当你没有为元素的属性指定值时该如何计算
值。

当元素的一个继承属性没有指定值时，则取父元素的同属性的计算值。只有文档根元素取该属性的概述中给定的初始值（这里的意思应
该是在该属性本身的定义中的默认值）。

当元素的一个非继承属性（在Mozilla code里有时称之为reset property）没有指定值时，则取属性的初始值initial v
alue（该值在该属性的概述里被指定）。

有继承性的属性：

（1）字体系列属性
font、font-family、font-weight、font-size、font-style、font-variant、font-stretch、font-size-adjust

（2）文本系列属性
text-indent、text-align、text-shadow、line-height、word-spacing、letter-spacing、
text-transform、direction、color

（3）表格布局属性
caption-side border-collapse empty-cells

（4）列表属性
list-style-type、list-style-image、list-style-position、list-style

（5）光标属性
cursor

（6）元素可见性
visibility

（7）还有一些不常用的；speak，page，设置嵌套引用的引号类型quotes等属性


注意：当一个属性不是继承属性时，可以使用inherit关键字指定一个属性应从父元素继承它的值，inherit关键字用于显式地
指定继承性，可用于任何继承性/非继承性属性。
```

回答：

```
每一个属性在定义中都给出了这个属性是否具有继承性，一个具有继承性的属性会在没有指定值的时候，会使用父元素的同属性的值
来作为自己的值。

一般具有继承性的属性有，字体相关的属性，font-size和font-weight等。文本相关的属性，color和text-align等。
表格的一些布局属性、列表属性如list-style等。还有光标属性cursor、元素可见性visibility。

当一个属性不是继承属性的时候，我们也可以通过将它的值设置为inherit来使它从父元素那获取同名的属性值来继承。
```

详细的资料可以参考：
[《继承属性》](https://developer.mozilla.org/zh-CN/docs/Web/CSS/inheritance)
[《CSS 有哪些属性可以继承？》](https://www.jianshu.com/p/34044e3c9317)

#### 6.CSS 优先级算法如何计算？

相关知识点：

```
CSS的优先级是根据样式声明的特殊性值来判断的。

选择器的特殊性值分为四个等级，如下：

（1）标签内选择符x,0,0,0
（2）ID选择符0,x,0,0
（3）class选择符/属性选择符/伪类选择符	0,0,x,0
（4）元素和伪元素选择符0,0,0,x

计算方法：

（1）每个等级的初始值为0
（2）每个等级的叠加为选择器出现的次数相加
（3）不可进位，比如0,99,99,99
（4）依次表示为：0,0,0,0
（5）每个等级计数之间没关联
（6）等级判断从左向右，如果某一位数值相同，则判断下一位数值
（7）如果两个优先级相同，则最后出现的优先级高，!important也适用
（8）通配符选择器的特殊性值为：0,0,0,0
（9）继承样式优先级最低，通配符样式优先级高于继承样式
（10）!important（权重），它没有特殊性值，但它的优先级是最高的，为了方便记忆，可以认为它的特殊性值为1,0,0,0,0。

计算实例：

（1）#demo a{color: orange;}/*特殊性值：0,1,0,1*/
（2）div#demo a{color: red;}/*特殊性值：0,1,0,2*/


注意：
（1）样式应用时，css会先查看规则的权重（!important），加了权重的优先级最高，当权重相同的时候，会比较规则的特殊性。

（2）特殊性值越大的声明优先级越高。

（3）相同特殊性值的声明，根据样式引入的顺序，后声明的规则优先级高（距离元素出现最近的）

 (4) 部分浏览器由于字节溢出问题出现的进位表现不做考虑
```

回答：

```
判断优先级时，首先我们会判断一条属性声明是否有权重，也就是是否在声明后面加上了!important。一条声明如果加上了权重，
那么它的优先级就是最高的，前提是它之后不再出现相同权重的声明。如果权重相同，我们则需要去比较匹配规则的特殊性。

一条匹配规则一般由多个选择器组成，一条规则的特殊性由组成它的选择器的特殊性累加而成。选择器的特殊性可以分为四个等级，
第一个等级是行内样式，为1000，第二个等级是id选择器，为0100，第三个等级是类选择器、伪类选择器和属性选择器，为0010，
第四个等级是元素选择器和伪元素选择器，为0001。规则中每出现一个选择器，就将它的特殊性进行叠加，这个叠加只限于对应的等
级的叠加，不会产生进位。选择器特殊性值的比较是从左向右排序的，也就是说以1开头的特殊性值比所有以0开头的特殊性值要大。
比如说特殊性值为1000的的规则优先级就要比特殊性值为0999的规则高。如果两个规则的特殊性值相等的时候，那么就会根据它们引
入的顺序，后出现的规则的优先级最高。
```

对于组合声明的特殊性值计算可以参考：
[《CSS 优先级计算及应用》](https://www.jianshu.com/p/1c4e639ff7d5)
[《CSS 优先级计算规则》](http://www.cnblogs.com/wangmeijian/p/4207433.html)
[《有趣：256 个 class 选择器可以干掉 1 个 id 选择器》](https://www.zhangxinxu.com/wordpress/2012/08/256-class-selector-beat-id-selector/)

#### 7.关于伪类 LVHA 的解释?

```
a标签有四种状态：链接访问前、链接访问后、鼠标滑过、激活，分别对应四种伪类:link、:visited、:hover、:active；

当链接未访问过时：

（1）当鼠标滑过a链接时，满足:link和:hover两种状态，要改变a标签的颜色，就必须将:hover伪类在:link伪
类后面声明；
（2）当鼠标点击激活a链接时，同时满足:link、:hover、:active三种状态，要显示a标签激活时的样式（:active），
必须将:active声明放到:link和:hover之后。因此得出LVHA这个顺序。

当链接访问过时，情况基本同上，只不过需要将:link换成:visited。

这个顺序能不能变？可以，但也只有:link和:visited可以交换位置，因为一个链接要么访问过要么没访问过，不可能同时满足，
也就不存在覆盖的问题。
```

#### 8.CSS3 新增伪类有那些？

```
（1）elem:nth-child(n)选中父元素下的第n个子元素，并且这个子元素的标签名为elem，n可以接受具体的数
值，也可以接受函数。

（2）elem:nth-last-child(n)作用同上，不过是从后开始查找。

（3）elem:last-child选中最后一个子元素。

（4）elem:only-child如果elem是父元素下唯一的子元素，则选中之。

（5）elem:nth-of-type(n)选中父元素下第n个elem类型元素，n可以接受具体的数值，也可以接受函数。

（6）elem:first-of-type选中父元素下第一个elem类型元素。

（7）elem:last-of-type选中父元素下最后一个elem类型元素。

（8）elem:only-of-type如果父元素下的子元素只有一个elem类型元素，则选中该元素。

（9）elem:empty选中不包含子元素和内容的elem类型元素。

（10）elem:target选择当前活动的elem元素。

（11）:not(elem)选择非elem元素的每个元素。

（12）:enabled 控制表单控件的禁用状态。

（13）:disabled	控制表单控件的禁用状态。

(14):checked单选框或复选框被选中。
```

详细的资料可以参考：
[《CSS3 新特性总结(伪类)》](https://www.cnblogs.com/SKLthegoodman/p/css3.html)
[《浅谈 CSS 伪类和伪元素及 CSS3 新增伪类》](https://blog.csdn.net/zhouziyu2011/article/details/58605705)

#### 9.如何居中 div？

-水平居中：给 div 设置一个宽度，然后添加 margin:0 auto 属性

```
div {
  width: 200px;
  margin: 0 auto;
}
```

-水平居中，利用 text-align:center 实现

```
.container {
  background: rgba(0, 0, 0, 0.5);
  text-align: center;
  font-size: 0;
}

.box {
  display: inline-block;
  width: 500px;
  height: 400px;
  background-color: pink;
}
```

-让绝对定位的 div 居中

```
div {
  position: absolute;
  width: 300px;
  height: 300px;
  margin: auto;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  background-color: pink; /*方便看效果*/
}
```

-水平垂直居中一

```
/*确定容器的宽高宽500高300的层设置层的外边距div{*/
position: absolute;/*绝对定位*/
width: 500px;
height: 300px;
top: 50%;
left: 50%;
margin: -150px 0 0 -250px;/*外边距为自身宽高的一半*/
background-color: pink;/*方便看效果*/
}
```

-水平垂直居中二

```
/*未知容器的宽高，利用`transform`属性*/
div {
  position: absolute; /*相对定位或绝对定位均可*/
  width: 500px;
  height: 300px;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: pink; /*方便看效果*/
}
```

-水平垂直居中三

```
/*利用flex布局实际使用时应考虑兼容性*/
.container {
  display: flex;
  align-items: center; /*垂直居中*/
  justify-content: center; /*水平居中*/
}
.containerdiv {
  width: 100px;
  height: 100px;
  background-color: pink; /*方便看效果*/
}
```

-水平垂直居中四

```
/*利用text-align:center和vertical-align:middle属性*/
.container {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background: rgba(0, 0, 0, 0.5);
  text-align: center;
  font-size: 0;
  white-space: nowrap;
  overflow: auto;
}

.container::after {
  content: '';
  display: inline-block;
  height: 100%;
  vertical-align: middle;
}

.box {
  display: inline-block;
  width: 500px;
  height: 400px;
  background-color: pink;
  white-space: normal;
  vertical-align: middle;
}
```

回答：

```
一般常见的几种居中的方法有：

对于宽高固定的元素

（1）我们可以利用margin:0 auto来实现元素的水平居中。

（2）利用绝对定位，设置四个方向的值都为0，并将margin设置为auto，由于宽高固定，因此对应方向实现平分，可以实现水
平和垂直方向上的居中。

（3）利用绝对定位，先将元素的左上角通过top:50%和left:50%定位到页面的中心，然后再通过margin负值来调整元素
的中心点到页面的中心。

（4）利用绝对定位，先将元素的左上角通过top:50%和left:50%定位到页面的中心，然后再通过translate来调整元素
的中心点到页面的中心。

（5）使用flex布局，通过align-items:center和justify-content:center设置容器的垂直和水平方向上为居中对
齐，然后它的子元素也可以实现垂直和水平的居中。

对于宽高不定的元素，上面的后面两种方法，可以实现元素的垂直和水平的居中。
```

#### 10.display 有哪些值？说明他们的作用。

```
block	块类型。默认宽度为父元素宽度，可设置宽高，换行显示。
none	元素不显示，并从文档流中移除。
inline	行内元素类型。默认宽度为内容宽度，不可设置宽高，同行显示。
inline-block 默认宽度为内容宽度，可以设置宽高，同行显示。
list-item	像块类型元素一样显示，并添加样式列表标记。
table	此元素会作为块级表格来显示。
inherit	规定应该从父元素继承display属性的值。
```

详细资料可以参考：
[《CSS display 属性》](http://www.w3school.com.cn/css/pr_class_display.asp)

#### 11.position 的值 relative 和 absolute 定位原点是？

相关知识点：

```
absolute
生成绝对定位的元素，相对于值不为static的第一个父元素的padding box进行定位，也可以理解为离自己这一级元素最近的
一级position设置为absolute或者relative的父元素的padding box的左上角为原点的。

fixed（老IE不支持）
生成绝对定位的元素，相对于浏览器窗口进行定位。

relative
生成相对定位的元素，相对于其元素本身所在正常位置进行定位。

static
默认值。没有定位，元素出现在正常的流中（忽略top,bottom,left,right,z-index声明）。

inherit
规定从父元素继承position属性的值。
```

回答：

```
relative定位的元素，是相对于元素本身的正常位置来进行定位的。

absolute定位的元素，是相对于它的第一个position值不为static的祖先元素的padding box来进行定位的。这句话
我们可以这样来理解，我们首先需要找到绝对定位元素的一个position的值不为static的祖先元素，然后相对于这个祖先元
素的padding box来定位，也就是说在计算定位距离的时候，padding的值也要算进去。
```

#### 12.CSS3 有哪些新特性？（根据项目回答）

```
新增各种CSS选择器	（:not(.input)：所有class不是“input”的节点）
圆角		（border-radius:8px）
多列布局	（multi-column layout）
阴影和反射	（Shadow\Reflect）
文字特效		（text-shadow）
文字渲染		（Text-decoration）
线性渐变		（gradient）
旋转			（transform）
缩放，定位，倾斜，动画，多背景
例如：transform:\scale(0.85,0.90)\translate(0px,-30px)\skew(-9deg,0deg)\Animation:
```

#### 13.请解释一下 CSS3 的 Flex box（弹性盒布局模型），以及适用场景？

相关知识点：

```
Flex是FlexibleBox的缩写，意为"弹性布局"，用来为盒状模型提供最大的灵活性。

任何一个容器都可以指定为Flex布局。行内元素也可以使用Flex布局。注意，设为Flex布局以后，子元素的float、cl
ear和vertical-align属性将失效。

采用Flex布局的元素，称为Flex容器（flex container），简称"容器"。它的所有子元素自动成为容器成员，称为Flex
项目（flex item），简称"项目"。

容器默认存在两根轴：水平的主轴（main axis）和垂直的交叉轴（cross axis），项目默认沿主轴排列。


以下6个属性设置在容器上。

flex-direction属性决定主轴的方向（即项目的排列方向）。

flex-wrap属性定义，如果一条轴线排不下，如何换行。

flex-flow属性是flex-direction属性和flex-wrap属性的简写形式，默认值为row nowrap。

justify-content属性定义了项目在主轴上的对齐方式。

align-items属性定义项目在交叉轴上如何对齐。

align-content属性定义了多根轴线的对齐方式。如果项目只有一根轴线，该属性不起作用。


以下6个属性设置在项目上。

order属性定义项目的排列顺序。数值越小，排列越靠前，默认为0。

flex-grow属性定义项目的放大比例，默认为0，即如果存在剩余空间，也不放大。

flex-shrink属性定义了项目的缩小比例，默认为1，即如果空间不足，该项目将缩小。

flex-basis属性定义了在分配多余空间之前，项目占据的主轴空间。浏览器根据这个属性，计算主轴是否有多余空间。它的默认
值为auto，即项目的本来大小。

flex属性是flex-grow，flex-shrink和flex-basis的简写，默认值为0 1 auto。

align-self属性允许单个项目有与其他项目不一样的对齐方式，可覆盖align-items属性。默认值为auto，表示继承父
元素的align-items属性，如果没有父元素，则等同于stretch。
```

回答：

```
flex布局是CSS3新增的一种布局方式，我们可以通过将一个元素的display属性值设置为flex从而使它成为一个flex
容器，它的所有子元素都会成为它的项目。

一个容器默认有两条轴，一个是水平的主轴，一个是与主轴垂直的交叉轴。我们可以使用flex-direction来指定主轴的方向。
我们可以使用justify-content来指定元素在主轴上的排列方式，使用align-items来指定元素在交叉轴上的排列方式。还
可以使用flex-wrap来规定当一行排列不下时的换行方式。

对于容器中的项目，我们可以使用order属性来指定项目的排列顺序，还可以使用flex-grow来指定当排列空间有剩余的时候，
项目的放大比例。还可以使用flex-shrink来指定当排列空间不足时，项目的缩小比例。
```

详细资料可以参考：
[《Flex 布局教程：语法篇》](http://www.ruanyifeng.com/blog/2015/07/flex-grammar.html)
[《Flex 布局教程：实例篇》](http://www.ruanyifeng.com/blog/2015/07/flex-examples.html)

#### 14.用纯 CSS 创建一个三角形的原理是什么？

```
采用的是相邻边框连接处的均分原理。
  将元素的宽高设为0，只设置
  border
  ，把任意三条边隐藏掉（颜色设为
  transparent），剩下的就是一个三角形。
  #demo {
  width: 0;
  height: 0;
  border-width: 20px;
  border-style: solid;
  border-color: transparent transparent red transparent;
}
```

#### 15.一个满屏品字布局如何设计?

```
简单的方式：
	上面的div宽100%，
	下面的两个div分别宽50%，
	然后用float或者inline使其不换行即可
```

#### 16.CSS 多列等高如何实现？

```
（1）利用padding-bottom|margin-bottom正负值相抵，不会影响页面布局的特点。设置父容器设置超出隐藏（overflow:
hidden），这样父容器的高度就还是它里面的列没有设定padding-bottom时的高度，当它里面的任一列高度增加了，则
父容器的高度被撑到里面最高那列的高度，其他比这列矮的列会用它们的padding-bottom补偿这部分高度差。

（2）利用table-cell所有单元格高度都相等的特性，来实现多列等高。

（3）利用flex布局中项目align-items属性默认为stretch，如果项目未设置高度或设为auto，将占满整个容器的高度
的特性，来实现多列等高。
```

详细资料可以参考：
[《前端应该掌握的 CSS 实现多列等高布局》](https://juejin.im/post/5b0fb34151882515662238fd)
[《CSS：多列等高布局》](https://codepen.io/yangbo5207/post/equh)

#### 17.经常遇到的浏览器的兼容性有哪些？原因，解决方法是什么，常用 hack 的技巧？

```
（1）png24位的图片在iE6浏览器上出现背景
解决方案：做成PNG8，也可以引用一段脚本处理。

（2）浏览器默认的margin和padding不同
解决方案：加一个全局的*{margin:0;padding:0;}来统一。

（3）IE6双边距bug：在IE6下，如果对元素设置了浮动，同时又设置了margin-left或
margin-right，margin值会加倍。

#box{float:left;width:10px;margin:0 0 0 10px;}

这种情况之下IE会产生20px的距离
解决方案：在float的标签样式控制中加入_display:inline;将其转化为行内属性。(_这个符号只有ie6会识别)

（4）渐进识别的方式，从总体中逐渐排除局部。
首先，巧妙的使用"\9"这一标记，将IE游览器从所有情况中分离出来。
接着，再次使用"+"将IE8和IE7、IE6分离开来，这样IE8已经独立识别。
.bb{
background-color:#f1ee18;/*所有识别*/
.background-color:#00deff\9;/*IE6、7、8识别*/
+background-color:#a200ff;/*IE6、7识别*/
_background-color:#1e0bd1;/*IE6识别*/
}

（5）IE下，可以使用获取常规属性的方法来获取自定义属性，也可以使用getAttribute()获取自定义
属性；Firefox下，只能使用getAttribute()获取自定义属性
解决方法：统一通过getAttribute()获取自定义属性。

（6）IE下，event对象有x、y属性，但是没有pageX、pageY属性;Firefox下，event对象有
pageX、pageY属性，但是没有x、y属性。
解决方法：（条件注释）缺点是在IE浏览器下可能会增加额外的HTTP请求数。

（7）Chrome中文界面下默认会将小于12px的文本强制按照12px显示
解决方法：

1.可通过加入CSS属性-webkit-text-size-adjust:none;解决。但是，在chrome
更新到27版本之后就不可以用了。

2.还可以使用-webkit-transform:scale(0.5);注意-webkit-transform:scale(0.75);
收缩的是整个span的大小，这时候，必须要将span转换成块元素，可以使用display：block/inline-block/...；

（8）超链接访问过后hover样式就不出现了，被点击访问过的超链接样式不再具有hover和active了
解决方法：改变CSS属性的排列顺序L-V-H-A

（9）怪异模式问题：漏写DTD声明，Firefox仍然会按照标准模式来解析网页，但在IE中会触发怪异模
式。为避免怪异模式给我们带来不必要的麻烦，最好养成书写DTD声明的好习惯。
```

#### 18.li 与 li 之间有看不见的空白间隔是什么原因引起的？有什么解决办法？

```
浏览器会把inline元素间的空白字符（空格、换行、Tab等）渲染成一个空格。而为了美观。我们通常是一个<li>放在一行，
这导致<li>换行后产生换行字符，它变成一个空格，占用了一个字符的宽度。

解决办法：

（1）为<li>设置float:left。不足：有些容器是不能设置浮动，如左右切换的焦点图等。

（2）将所有<li>写在同一行。不足：代码不美观。

（3）将<ul>内的字符尺寸直接设为0，即font-size:0。不足：<ul>中的其他字符尺寸也被设为0，需要额外重新设定其他
字符尺寸，且在Safari浏览器依然会出现空白间隔。

（4）消除<ul>的字符间隔letter-spacing:-8px，不足：这也设置了<li>内的字符间隔，因此需要将<li>内的字符
间隔设为默认letter-spacing:normal。
```

详细资料可以参考：
[《li 与 li 之间有看不见的空白间隔是什么原因引起的？》](https://blog.csdn.net/sjinsa/article/details/70919546)

#### 19.为什么要初始化 CSS 样式？

```
-因为浏览器的兼容问题，不同浏览器对有些标签的默认值是不同的，如果没对CSS初始化往往会出现浏览器之间的页面显示差异。

-当然，初始化样式会对SEO有一定的影响，但鱼和熊掌不可兼得，但力求影响最小的情况下初始化。

最简单的初始化方法：*{padding:0;margin:0;}（强烈不建议）

淘宝的样式初始化代码：
body,h1,h2,h3,h4,h5,h6,hr,p,blockquote,dl,dt,dd,ul,ol,li,pre,form,fieldset,legend
,button,input,textarea,th,td{margin:0;padding:0;}
body,button,input,select,textarea{font:12px/1.5tahoma,arial,\5b8b\4f53;}
h1,h2,h3,h4,h5,h6{font-size:100%;}
address,cite,dfn,em,var{font-style:normal;}
code,kbd,pre,samp{font-family:couriernew,courier,monospace;}
small{font-size:12px;}
ul,ol{list-style:none;}
a{text-decoration:none;}
a:hover{text-decoration:underline;}
sup{vertical-align:text-top;}
sub{vertical-align:text-bottom;}
legend{color:#000;}
fieldset,img{border:0;}
button,input,select,textarea{font-size:100%;}
table{border-collapse:collapse;border-spacing:0;}
```

#### 20.什么是包含块，对于包含块的理解?

```
包含块（containing block）就是元素用来计算和定位的一个框。

（1）根元素（很多场景下可以看成是<html>）被称为“初始包含块”，其尺寸等同于浏览器可视窗口的大小。

（2）对于其他元素，如果该元素的position是relative或者static，则“包含块”由其最近的块容器祖先盒的content box
边界形成。

（3）如果元素position:fixed，则“包含块”是“初始包含块”。

（4）如果元素position:absolute，则“包含块”由最近的position不为static的祖先元素建立，具体方式如下：

如果该祖先元素是纯inline元素，则规则略复杂：
•假设给内联元素的前后各生成一个宽度为0的内联盒子（inline box），则这两个内联盒子的padding box外面的包
围盒就是内联元素的“包含块”；
•如果该内联元素被跨行分割了，那么“包含块”是未定义的，也就是CSS2.1规范并没有明确定义，浏览器自行发挥
否则，“包含块”由该祖先的padding box边界形成。

如果没有符合条件的祖先元素，则“包含块”是“初始包含块”。
```

#### 21.CSS 里的 visibility 属性有个 collapse 属性值是干嘛用的？在不同浏览器下以后什么区别？

```
（1）对于一般的元素，它的表现跟visibility：hidden;是一样的。元素是不可见的，但此时仍占用页面空间。

（2）但例外的是，如果这个元素是table相关的元素，例如table行，table group，table列，table column group，它的
表现却跟display:none一样，也就是说，它们占用的空间也会释放。

在不同浏览器下的区别：

在谷歌浏览器里，使用collapse值和使用hidden值没有什么区别。

在火狐浏览器、Opera和IE11里，使用collapse值的效果就如它的字面意思：table的行会消失，它的下面一行会补充它的位
置。
```

详细资料可以参考：
[《CSS 里的 visibility 属性有个鲜为人知的属性值：collapse》](http://www.webhek.com/post/visibility-collapse.html)

#### 22.width:auto 和 width:100%的区别

```
一般而言

width:100%会使元素box的宽度等于父元素的content box的宽度。

width:auto会使元素撑满整个父元素，margin、border、padding、content区域会自动分配水平空间。
```

#### 23.绝对定位元素与非绝对定位元素的百分比计算的区别

```
绝对定位元素的宽高百分比是相对于临近的position不为static的祖先元素的padding box来计算的。

非绝对定位元素的宽高百分比则是相对于父元素的content box来计算的。
```

#### 24.简单介绍使用图片 base64 编码的优点和缺点。

```
base64编码是一种图片处理格式，通过特定的算法将图片编码成一长串字符串，在页面上显示的时候，可以用该字符串来代替图片的
url属性。

使用base64的优点是：

（1）减少一个图片的HTTP请求

使用base64的缺点是：

（1）根据base64的编码原理，编码后的大小会比原文件大小大1/3，如果把大图片编码到html/css中，不仅会造成文件体
积的增加，影响文件的加载速度，还会增加浏览器对html或css文件解析渲染的时间。

（2）使用base64无法直接缓存，要缓存只能缓存包含base64的文件，比如HTML或者CSS，这相比域直接缓存图片的效果要
差很多。

（3）兼容性的问题，ie8以前的浏览器不支持。

一般一些网站的小图标可以使用base64图片来引入。
```

详细资料可以参考：
[《玩转图片 base64 编码》](https://www.cnblogs.com/coco1s/p/4375774.html)
[《前端开发中，使用 base64 图片的弊端是什么？》](https://www.zhihu.com/question/31155574)
[《小 tip:base64:URL 背景图片与 web 页面性能优化》](https://www.zhangxinxu.com/wordpress/2012/04/base64-url-image-图片-页面性能优化/)

#### 25.’display’、’position’和’float’的相互关系？

```
（1）首先我们判断display属性是否为none，如果为none，则position和float属性的值不影响元素最后的表现。

（2）然后判断position的值是否为absolute或者fixed，如果是，则float属性失效，并且display的值应该被
设置为table或者block，具体转换需要看初始转换值。

（3）如果position的值不为absolute或者fixed，则判断float属性的值是否为none，如果不是，则display
的值则按上面的规则转换。注意，如果position的值为relative并且float属性的值存在，则relative相对
于浮动后的最终位置定位。

（4）如果float的值为none，则判断元素是否为根元素，如果是根元素则display属性按照上面的规则转换，如果不是，
则保持指定的display属性值不变。

总的来说，可以把它看作是一个类似优先级的机制，"position:absolute"和"position:fixed"优先级最高，有它存在
的时候，浮动不起作用，'display'的值也需要调整；其次，元素的'float'特性的值不是"none"的时候或者它是根元素
的时候，调整'display'的值；最后，非根元素，并且非浮动元素，并且非绝对定位的元素，'display'特性值同设置值。
```

详细资料可以参考：
[《position 跟 display、margincollapse、overflow、float 这些特性相互叠加后会怎么样？》](https://www.cnblogs.com/jackyWHJ/p/3756087.html)

#### 26.margin 重叠问题的理解。

相关知识点：

```
块级元素的上外边距（margin-top）与下外边距（margin-bottom）有时会合并为单个外边距，这样的现象称为“margin合
并”。

产生折叠的必备条件：margin必须是邻接的!

而根据w3c规范，两个margin是邻接的必须满足以下条件：

•必须是处于常规文档流（非float和绝对定位）的块级盒子，并且处于同一个BFC当中。
•没有线盒，没有空隙，没有padding和border将他们分隔开
•都属于垂直方向上相邻的外边距，可以是下面任意一种情况
•元素的margin-top与其第一个常规文档流的子元素的margin-top
•元素的margin-bottom与其下一个常规文档流的兄弟元素的margin-top
•height为auto的元素的margin-bottom与其最后一个常规文档流的子元素的margin-bottom
•高度为0并且最小高度也为0，不包含常规文档流的子元素，并且自身没有建立新的BFC的元素的margin-top
和margin-bottom


margin合并的3种场景：

（1）相邻兄弟元素margin合并。

解决办法：
•设置块状格式化上下文元素（BFC）

（2）父级和第一个/最后一个子元素的margin合并。

解决办法：

对于margin-top合并，可以进行如下操作（满足一个条件即可）：
•父元素设置为块状格式化上下文元素；
•父元素设置border-top值；
•父元素设置padding-top值；
•父元素和第一个子元素之间添加内联元素进行分隔。

对于margin-bottom合并，可以进行如下操作（满足一个条件即可）：
•父元素设置为块状格式化上下文元素；
•父元素设置border-bottom值；
•父元素设置padding-bottom值；
•父元素和最后一个子元素之间添加内联元素进行分隔；
•父元素设置height、min-height或max-height。

（3）空块级元素的margin合并。

解决办法：
•设置垂直方向的border；
•设置垂直方向的padding；
•里面添加内联元素（直接Space键空格是没用的）；
•设置height或者min-height。
```

回答：

```
margin重叠指的是在垂直方向上，两个相邻元素的margin发生重叠的情况。

一般来说可以分为四种情形：

第一种是相邻兄弟元素的marin-bottom和margin-top的值发生重叠。这种情况下我们可以通过设置其中一个元素为BFC
来解决。

第二种是父元素的margin-top和子元素的margin-top发生重叠。它们发生重叠是因为它们是相邻的，所以我们可以通过这
一点来解决这个问题。我们可以为父元素设置border-top、padding-top值来分隔它们，当然我们也可以将父元素设置为BFC
来解决。

第三种是高度为auto的父元素的margin-bottom和子元素的margin-bottom发生重叠。它们发生重叠一个是因为它们相
邻，一个是因为父元素的高度不固定。因此我们可以为父元素设置border-bottom、padding-bottom来分隔它们，也可以为
父元素设置一个高度，max-height和min-height也能解决这个问题。当然将父元素设置为BFC是最简单的方法。

第四种情况，是没有内容的元素，自身的margin-top和margin-bottom发生的重叠。我们可以通过为其设置border、pa
dding或者高度来解决这个问题。
```

#### 27.对 BFC 规范（块级格式化上下文：block formatting context）的理解？

相关知识点：

```
块格式化上下文（Block Formatting Context，BFC）是Web页面的可视化CSS渲染的一部分，是布局过程中生成块级盒
子的区域，也是浮动元素与其他元素的交互限定区域。

通俗来讲

•BFC是一个独立的布局环境，可以理解为一个容器，在这个容器中按照一定规则进行物品摆放，并且不会影响其它环境中的物品。
•如果一个元素符合触发BFC的条件，则BFC中的元素布局不受外部影响。

创建BFC

（1）根元素或包含根元素的元素
（2）浮动元素float＝left|right或inherit（≠none）
（3）绝对定位元素position＝absolute或fixed
（4）display＝inline-block|flex|inline-flex|table-cell或table-caption
（5）overflow＝hidden|auto或scroll(≠visible)
```

回答：

```
BFC指的是块级格式化上下文，一个元素形成了BFC之后，那么它内部元素产生的布局不会影响到外部元素，外部元素的布局也
不会影响到BFC中的内部元素。一个BFC就像是一个隔离区域，和其他区域互不影响。

一般来说根元素是一个BFC区域，浮动和绝对定位的元素也会形成BFC，display属性的值为inline-block、flex这些
属性时也会创建BFC。还有就是元素的overflow的值不为visible时都会创建BFC。
```

详细资料可以参考：
[《深入理解 BFC 和 MarginCollapse》](https://www.w3cplus.com/css/understanding-bfc-and-margin-collapse.html)
[《前端面试题-BFC（块格式化上下文）》](https://segmentfault.com/a/1190000013647777)

#### 28.IFC 是什么？

```
IFC指的是行级格式化上下文，它有这样的一些布局规则：

（1）行级上下文内部的盒子会在水平方向，一个接一个地放置。
（2）当一行不够的时候会自动切换到下一行。
（3）行级上下文的高度由内部最高的内联盒子的高度决定。
```

详细资料可以参考：
[《[译\]:BFC 与 IFC》](https://segmentfault.com/a/1190000004466536#articleHeader5)
[《BFC 和 IFC 的理解（布局）》](https://blog.csdn.net/paintandraw/article/details/80401741)

#### 29.请解释一下为什么需要清除浮动？清除浮动的方式

```
浮动元素可以左右移动，直到遇到另一个浮动元素或者遇到它外边缘的包含框。浮动框不属于文档流中的普通流，当元素浮动之后，
不会影响块级元素的布局，只会影响内联元素布局。此时文档流中的普通流就会表现得该浮动框不存在一样的布局模式。当包含框
的高度小于浮动框的时候，此时就会出现“高度塌陷”。

清除浮动是为了清除使用浮动元素产生的影响。浮动的元素，高度会塌陷，而高度的塌陷使我们页面后面的布局不能正常显示。

清除浮动的方式

（1）使用clear属性清除浮动。参考28。

（2）使用BFC块级格式化上下文来清除浮动。参考26。

因为BFC元素不会影响外部元素的特点，所以BFC元素也可以用来清除浮动的影响，因为如果不清除，子元素浮动则父元
素高度塌陷，必然会影响后面元素布局和定位，这显然有违BFC元素的子元素不会影响外部元素的设定。
```

#### 30.使用 clear 属性清除浮动的原理？

```
使用clear属性清除浮动，其语法如下：

clear:none|left|right|both

如果单看字面意思，clear:left应该是“清除左浮动”，clear:right应该是“清除右浮动”的意思，实际上，这种解释是有问
题的，因为浮动一直还在，并没有清除。

官方对clear属性的解释是：“元素盒子的边不能和前面的浮动元素相邻。”，我们对元素设置clear属性是为了避免浮动元素
对该元素的影响，而不是清除掉浮动。

还需要注意的一点是clear属性指的是元素盒子的边不能和前面的浮动元素相邻，注意这里“前面的”3个字，也就是clear属
性对“后面的”浮动元素是不闻不问的。考虑到float属性要么是left，要么是right，不可能同时存在，同时由于clear
属性对“后面的”浮动元素不闻不问，因此，当clear:left有效的时候，clear:right必定无效，也就是此时clear:left
等同于设置clear:both；同样地，clear:right如果有效也是等同于设置clear:both。由此可见，clear:left和cle
ar:right这两个声明就没有任何使用的价值，至少在CSS世界中是如此，直接使用clear:both吧。

一般使用伪元素的方式清除浮动

.clear::after{
content:'';
display:table;//也可以是'block'，或者是'list-item'
clear:both;
}

clear属性只有块级元素才有效的，而::after等伪元素默认都是内联水平，这就是借助伪元素清除浮动影响时需要设置disp
lay属性值的原因。
```

#### 31.zoom:1 的清除浮动原理?

```
清除浮动，触发hasLayout；
zoom属性是IE浏览器的专有属性，它可以设置或检索对象的缩放比例。解决ie下比较奇葩的bug。譬如外边距（margin）
的重叠，浮动清除，触发ie的haslayout属性等。

来龙去脉大概如下：
当设置了zoom的值之后，所设置的元素就会就会扩大或者缩小，高度宽度就会重新计算了，这里一旦改变zoom值时其实也会发
生重新渲染，运用这个原理，也就解决了ie下子元素浮动时候父元素不随着自动扩大的问题。

zoom属性是IE浏览器的专有属性，火狐和老版本的webkit核心的浏览器都不支持这个属性。然而，zoom现在已经被逐步标
准化，出现在CSS3.0规范草案中。

目前非ie由于不支持这个属性，它们又是通过什么属性来实现元素的缩放呢？可以通过css3里面的动画属性scale进行缩放。
```

#### 32.移动端的布局用过媒体查询吗？

```
假设你现在正用一台显示设备来阅读这篇文章，同时你也想把它投影到屏幕上，或者打印出来，而显示设备、屏幕投影和打印等这些
媒介都有自己的特点，CSS就是为文档提供在不同媒介上展示的适配方法

当媒体查询为真时，相关的样式表或样式规则会按照正常的级联规被应用。当媒体查询返回假，标签上带有媒体查询的样式表仍将被
下载（只不过不会被应用）。

包含了一个媒体类型和至少一个使用宽度、高度和颜色等媒体属性来限制样式表范围的表达式。CSS3加入的媒体查询使得无需修改
内容便可以使样式应用于某些特定的设备范围。
```

详细资料可以参考：
[《CSS3@media 查询》](http://www.runoob.com/cssref/css3-pr-mediaquery.html)
[《响应式布局和自适应布局详解》](http://caibaojian.com/356.html)

#### 33.使用 CSS 预处理器吗？喜欢哪个？

```
SASS（SASS、LESS没有本质区别，只因为团队前端都是用的SASS）
```

#### 34.CSS 优化、提高性能的方法有哪些？

```
加载性能：

（1）css压缩：将写好的css进行打包压缩，可以减少很多的体积。
（2）css单一样式：当需要下边距和左边距的时候，很多时候选择:margin:top 0 bottom 0;但margin-bottom:bot
tom;margin-left:left;执行的效率更高。
（3）减少使用@import,而建议使用link，因为后者在页面加载时一起加载，前者是等待页面加载完成之后再进行加载。

选择器性能：

（1）关键选择器（key selector）。选择器的最后面的部分为关键选择器（即用来匹配目标元素的部分）。CSS选择符是从右到
左进行匹配的。当使用后代选择器的时候，浏览器会遍历所有子元素来确定是否是指定的元素等等；

（2）如果规则拥有ID选择器作为其关键选择器，则不要为规则增加标签。过滤掉无关的规则（这样样式系统就不会浪费时间去匹
配它们了）。

（3）避免使用通配规则，如*{}计算次数惊人！只对需要用到的元素进行选择。

（4）尽量少的去对标签进行选择，而是用class。

（5）尽量少的去使用后代选择器，降低选择器的权重值。后代选择器的开销是最高的，尽量将选择器的深度降到最低，最高不要超过
三层，更多的使用类来关联每一个标签元素。

（6）了解哪些属性是可以通过继承而来的，然后避免对这些属性重复指定规则。

渲染性能：

（1）慎重使用高性能属性：浮动、定位。

（2）尽量减少页面重排、重绘。

（3）去除空规则：｛｝。空规则的产生原因一般来说是为了预留样式。去除这些空规则无疑能减少css文档体积。

（4）属性值为0时，不加单位。

（5）属性值为浮动小数0.**，可以省略小数点之前的0。

（6）标准化各种浏览器前缀：带浏览器前缀的在前。标准属性在后。

（7）不使用@import前缀，它会影响css的加载速度。

（8）选择器优化嵌套，尽量避免层级过深。

（9）css雪碧图，同一页面相近部分的小图标，方便使用，减少页面的请求次数，但是同时图片本身会变大，使用时，优劣考虑清
楚，再使用。

（10）正确使用display的属性，由于display的作用，某些样式组合会无效，徒增样式体积的同时也影响解析性能。

（11）不滥用web字体。对于中文网站来说WebFonts可能很陌生，国外却很流行。web fonts通常体积庞大，而且一些浏
览器在下载web fonts时会阻塞页面渲染损伤性能。

可维护性、健壮性：

（1）将具有相同属性的样式抽离出来，整合并通过class在页面中进行使用，提高css的可维护性。
（2）样式与内容分离：将css代码定义到外部css中。
```

详细资料可以参考：
[《CSS 优化、提高性能的方法有哪些？》](https://www.zhihu.com/question/19886806)
[《CSS 优化，提高性能的方法》](https://www.jianshu.com/p/4e673bf24a3b)

#### 35.浏览器是怎样解析 CSS 选择器的？

```
样式系统从关键选择器开始匹配，然后左移查找规则选择器的祖先元素。只要选择器的子树一直在工作，样式系统就会持续左移，直
到和规则匹配，或者是因为不匹配而放弃该规则。

试想一下，如果采用从左至右的方式读取CSS规则，那么大多数规则读到最后（最右）才会发现是不匹配的，这样做会费时耗能，
最后有很多都是无用的；而如果采取从右向左的方式，那么只要发现最右边选择器不匹配，就可以直接舍弃了，避免了许多无效匹配。
```

详细资料可以参考：
[《探究 CSS 解析原理》](https://juejin.im/entry/5a123c55f265da432240cc90)

#### 36.在网页中应该使用奇数还是偶数的字体？为什么呢？

```
（1）偶数字号相对更容易和web设计的其他部分构成比例关系。比如：当我用了14px的正文字号，我可能会在一些地方用14
×0.5=7px的margin，在另一些地方用14×1.5=21px的标题字号。
（2）浏览器缘故，低版本的浏览器ie6会把奇数字体强制转化为偶数，即13px渲染为14px。
（3）系统差别，早期的Windows里，中易宋体点阵只有12和14、15、16px，唯独缺少13px。
```

详细资料可以参考：
[《谈谈网页中使用奇数字体和偶数字体》](https://blog.csdn.net/jian_xi/article/details/79346477)
[《现在网页设计中的为什么少有人用 11px、13px、15px 等奇数的字体？》](https://www.zhihu.com/question/20440679)

#### 37.margin 和 padding 分别适合什么场景使用？

```
margin是用来隔开元素与元素的间距；padding是用来隔开元素与内容的间隔。
margin用于布局分开元素使元素与元素互不相干。
padding用于元素与内容之间的间隔，让内容（文字）与（包裹）元素之间有一段距离。

何时应当使用margin：
•需要在border外侧添加空白时。
•空白处不需要背景（色）时。
•上下相连的两个盒子之间的空白，需要相互抵消时。如15px+20px的margin，将得到20px的空白。

何时应当时用padding：
•需要在border内测添加空白时。
•空白处需要背景（色）时。
•上下相连的两个盒子之间的空白，希望等于两者之和时。如15px+20px的padding，将得到35px的空白。
```

#### 38.抽离样式模块怎么写，说出思路，有无实践经验？[阿里航旅的面试题]

```
我的理解是把常用的css样式单独做成css文件……通用的和业务相关的分离出来，通用的做成样式模块儿共享，业务相关的，放
进业务相关的库里面做成对应功能的模块儿。
```

详细资料可以参考：
[《CSS 规范-分类方法》](http://nec.netease.com/standard/css-sort.html)

#### 39.简单说一下 css3 的 all 属性。

```
all属性实际上是所有CSS属性的缩写，表示，所有的CSS属性都怎样怎样，但是，不包括unicode-bidi和direction
这两个CSS属性。支持三个CSS通用属性值，initial,inherit,unset。

initial是初始值的意思，也就是该元素元素都除了unicode-bidi和direction以外的CSS属性都使用属性的默认初始
值。

inherit是继承的意思，也就是该元素除了unicode-bidi和direction以外的CSS属性都继承父元素的属性值。

unset是取消设置的意思，也就是当前元素浏览器或用户设置的CSS忽略，然后如果是具有继承特性的CSS，如color，则
使用继承值；如果是没有继承特性的CSS属性，如background-color，则使用初始值。
```

详细资料可以参考：
[《简单了解 CSS3 的 all 属性》](https://www.zhangxinxu.com/wordpress/2016/03/know-about-css3-all/)

#### 40.为什么不建议使用统配符初始化 css 样式。

```
采用*{padding:0;margin:0;}这样的写法好处是写起来很简单，但是是通配符，需要把所有的标签都遍历一遍，当网站较大时，
样式比较多，这样写就大大的加强了网站运行的负载，会使网站加载的时候需要很长一段时间，因此一般大型的网站都有分层次的一
套初始化样式。

出于性能的考虑，并不是所有标签都会有padding和margin，因此对常见的具有默认padding和margin的元素初始化即
可，并不需使用通配符*来初始化。
```

#### 41.absolute 的 containingblock（包含块）计算方式跟正常流有什么不同？

```
（1）内联元素也可以作为“包含块”所在的元素；

（2）“包含块”所在的元素不是父块级元素，而是最近的position不为static的祖先元素或根元素；

（3）边界是padding box而不是content box。
```

#### 42.对于 hasLayout 的理解？

```
hasLayout是IE特有的一个属性。很多的IE下的css bug都与其息息相关。在IE中，一个元素要么自己对自身的内容进
行计算大小和组织，要么依赖于父元素来计算尺寸和组织内容。当一个元素的hasLayout属性值为true时，它负责对自己和可
能的子孙元素进行尺寸计算和定位。虽然这意味着这个元素需要花更多的代价来维护自身和里面的内容，而不是依赖于祖先元素来完
成这些工作。
```

详细资料可以参考：
[《CSS 基础篇–CSS 中 IE 浏览器的 hasLayout，IE 低版本的 bug 根源》](https://segmentfault.com/a/1190000010883974)
[《CSS 魔法堂：hasLayout 原来是这样的！》](https://segmentfault.com/a/1190000004632071)

#### 43.元素竖向的百分比设定是相对于容器的高度吗？

```
如果是height的话，是相对于包含块的高度。

如果是padding或者margin竖直方向的属性则是相对于包含块的宽度。
```

#### 44.全屏滚动的原理是什么？用到了 CSS 的哪些属性？（待深入实践）

```
原理：有点类似于轮播，整体的元素一直排列下去，假设有5个需要展示的全屏页面，那么高度是500%，只是展示100%，容器及容
器内的页面取当前可视区高度，同时容器的父级元素overflow属性值设为hidden，通过更改容器可视区的位置来实现全
屏滚动效果。主要是响应鼠标事件，页面通过CSS的动画效果，进行移动。

overflow：hidden；transition：all 1000 ms ease；
```

详细资料可以参考：
[《js 实现网页全屏切换（平滑过渡），鼠标滚动切换》](https://blog.csdn.net/liona_koukou/article/details/52680409)
[《用 ES6 写全屏滚动插件》](https://juejin.im/post/5aeef41cf265da0ba0630de0)

#### 45.什么是响应式设计？响应式设计的基本原理是什么？如何兼容低版本的 IE？（待深入了解）

```
响应式网站设计是一个网站能够兼容多个终端，而不是为每一个终端做一个特定的版本。基本原理是通过媒体查询检测不同的设备屏
幕尺寸做处理。页面头部必须有meta声明的viewport。
```

详细资料可以参考：
[《响应式布局原理》](https://blog.csdn.net/dreamerframework/article/details/8994741)
[《响应式布局的实现方法和原理》](http://www.mahaixiang.cn/wzsj/278.html)

#### 46.视差滚动效果，如何给每页做不同的动画？（回到顶部，向下滑动要再次出现，和只出现一次分别怎么做？）

```
视差滚动是指多层背景以不同的速度移动，形成立体的运动效果，带来非常出色的视觉体验。
```

详细资料可以参考：
[《如何实现视差滚动效果的网页？》](https://www.zhihu.com/question/20990029)

#### 47.如何修改 chrome 记住密码后自动填充表单的黄色背景？

```
chrome表单自动填充后，input文本框的背景会变成黄色的，通过审查元素可以看到这是由于chrome会默认给自动填充的in
put表单加上input:-webkit-autofill私有属性，然后对其赋予以下样式：

{
background-color:rgb(250,255,189)!important;
background-image:none!important;
color:rgb(0,0,0)!important;
}

对chrome默认定义的background-color，background-image，color使用important是不能提高其优先级的，但是
其他属性可使用。

使用足够大的纯色内阴影来覆盖input输入框的黄色背景，处理如下

input:-webkit-autofill,textarea:-webkit-autofill,select:-webkit-autofill{
-webkit-box-shadow:000px 1000px white inset;
border:1px solid #CCC !important;
}
```

详细资料可以参考：
[《去掉 chrome 记住密码后的默认填充样式》](https://blog.csdn.net/zsl_955200/article/details/78276209)
[《修改谷歌浏览器 chrome 记住密码后自动填充表单的黄色背景》](https://blog.csdn.net/M_agician/article/details/73381706)

#### 48.怎么让 Chrome 支持小于 12px 的文字？

```
在谷歌下css设置字体大小为12px及以下时，显示都是一样大小，都是默认12px。

解决办法：

（1）可以使用Webkit的内核的-webkit-text-size-adjust的私有CSS属性来解决，只要加了-webkit-text-size
-adjust:none;字体大小就不受限制了。但是chrome更新到27版本之后就不可以用了。所以高版本chrome谷歌浏览器
已经不再支持-webkit-text-size-adjust样式，所以要使用时候慎用。

（2）还可以使用css3的transform缩放属性-webkit-transform:scale(0.5);注意-webkit-transform:scale(0.
75);收缩的是整个元素的大小，这时候，如果是内联元素，必须要将内联元素转换成块元素，可以使用display：block/
inline-block/...；

（3）使用图片：如果是内容固定不变情况下，使用将小于12px文字内容切出做图片，这样不影响兼容也不影响美观。
```

详细资料可以参考：
[《谷歌浏览器不支持 CSS 设置小于 12px 的文字怎么办？》](https://570109268.iteye.com/blog/2406562)

#### 49.让页面里的字体变清晰，变细用 CSS 怎么做？

```
webkit内核的私有属性：-webkit-font-smoothing，用于字体抗锯齿，使用后字体看起来会更清晰舒服。

在MacOS测试环境下面设置-webkit-font-smoothing:antialiased;但是这个属性仅仅是面向MacOS，其他操作系统设
置后无效。
```

详细资料可以参考：
[《让字体变的更清晰 CSS 中-webkit-font-smoothing》](https://blog.csdn.net/huo_bao/article/details/50251585)

#### 50.font-style 属性中 italic 和 oblique 的区别？

```
italic和oblique这两个关键字都表示“斜体”的意思。

它们的区别在于，italic是使用当前字体的斜体字体，而oblique只是单纯地让文字倾斜。如果当前字体没有对应的斜体字体，
则退而求其次，解析为oblique，也就是单纯形状倾斜。
```

#### 51.设备像素、css 像素、设备独立像素、dpr、ppi 之间的区别？

```
设备像素指的是物理像素，一般手机的分辨率指的就是设备像素，一个设备的设备像素是不可变的。

css像素和设备独立像素是等价的，不管在何种分辨率的设备上，css像素的大小应该是一致的，css像素是一个相对单位，它是相
对于设备像素的，一个css像素的大小取决于页面缩放程度和dpr的大小。

dpr指的是设备像素和设备独立像素的比值，一般的pc屏幕，dpr=1。在iphone4时，苹果推出了retina屏幕，它的dpr
为2。屏幕的缩放会改变dpr的值。

ppi指的是每英寸的物理像素的密度，ppi越大，屏幕的分辨率越大。
```

详细资料可以参考：
[《什么是物理像素、虚拟像素、逻辑像素、设备像素，什么又是 PPI,DPI,DPR 和 DIP》](https://www.cnblogs.com/libin-1/p/7148377.html)
[《前端工程师需要明白的「像素」》](https://www.jianshu.com/p/af6dad66e49a)
[《CSS 像素、物理像素、逻辑像素、设备像素比、PPI、Viewport》](https://github.com/jawil/blog/issues/21)
[《前端开发中像素的概念》](https://github.com/wujunchuan/wujunchuan.github.io/issues/15)

#### 52.layout viewport、visual viewport 和 ideal viewport 的区别？

相关知识点：

```
如果把移动设备上浏览器的可视区域设为viewport的话，某些网站就会因为viewport太窄而显示错乱，所以这些浏览器就决定
默认情况下把viewport设为一个较宽的值，比如980px，这样的话即使是那些为桌面设计的网站也能在移动浏览器上正常显示了。
ppk把这个浏览器默认的viewport叫做layout viewport。

layout viewport的宽度是大于浏览器可视区域的宽度的，所以我们还需要一个viewport来代表浏览器可视区域的大小，ppk把
这个viewport叫做visual viewport。

ideal viewport是最适合移动设备的viewport，ideal viewport的宽度等于移动设备的屏幕宽度，只要在css中把某一元
素的宽度设为ideal viewport的宽度（单位用px），那么这个元素的宽度就是设备屏幕的宽度了，也就是宽度为100%的效果。i
deal viewport的意义在于，无论在何种分辨率的屏幕下，那些针对ideal viewport而设计的网站，不需要用户手动缩放，也
不需要出现横向滚动条，都可以完美的呈现给用户。
```

回答：

```
移动端一共需要理解三个viewport的概念的理解。

第一个视口是布局视口，在移动端显示网页时，由于移动端的屏幕尺寸比较小，如果网页使用移动端的屏幕尺寸进行布局的话，那么整
个页面的布局都会显示错乱。所以移动端浏览器提供了一个layout viewport布局视口的概念，使用这个视口来对页面进行布局展
示，一般layout viewport的大小为980px，因此页面布局不会有太大的变化，我们可以通过拖动和缩放来查看到这个页面。

第二个视口指的是视觉视口，visual viewport指的是移动设备上我们可见的区域的视口大小，一般为屏幕的分辨率的大小。visu
al viewport和layout viewport的关系，就像是我们通过窗户看外面的风景，视觉视口就是窗户，而外面的风景就是布局视口
中的网页内容。

第三个视口是理想视口，由于layout viewport一般比visual viewport要大，所以想要看到整个页面必须通过拖动和缩放才
能实现。所以又提出了ideal viewport的概念，ideal viewport下用户不用缩放和滚动条就能够查看到整个页面，并且页面在
不同分辨率下显示的内容大小相同。ideal viewport其实就是通过修改layout viewport的大小，让它等于设备的宽度，这个
宽度可以理解为是设备独立像素，因此根据ideal viewport设计的页面，在不同分辨率的屏幕下，显示应该相同。
```

详细资料可以参考：
[《移动前端开发之 viewport 的深入理解》](https://www.cnblogs.com/2050/p/3877280.html)
[《说说移动前端中 viewport（视口）》](https://www.html.cn/archives/5975)
[《移动端适配知识你到底知多少》](https://juejin.im/post/5b6d21daf265da0f9d1a2ed7#heading-14)

#### 53.position:fixed;在 android 下无效怎么处理？

```
因为移动端浏览器默认的viewport叫做layout viewport。在移动端显示时，因为layout viewport的宽度大于移动端屏幕
的宽度，所以页面会出现滚动条左右移动，fixed的元素是相对layout viewport来固定位置的，而不是移动端屏幕来固定位置的
，所以会出现感觉fixed无效的情况。

如果想实现fixed相对于屏幕的固定效果，我们需要改变的是viewport的大小为ideal viewport，可以如下设置：

<metaname="viewport"content="width=device-width,initial-scale=1.0,maximum-scale=1.0,minimum-sca
le=1.0,user-scalable=no"/>
```

#### 54.如果需要手动写动画，你认为最小时间间隔是多久，为什么？（阿里）

```
多数显示器默认频率是60Hz，即1秒刷新60次，所以理论上最小间隔为1/60*1000ms＝16.7ms
```

#### 55.如何让去除 inline-block 元素间间距？

```
移除空格、使用margin负值、使用font-size:0、letter-spacing、word-spacing
```

详细资料可以参考：
[《去除 inline-block 元素间间距的 N 种方法》](https://www.zhangxinxu.com/wordpress/2012/04/inline-block-space-remove-去除间距/)

#### 56.overflow:scroll 时不能平滑滚动的问题怎么处理？

```
以下代码可解决这种卡顿的问题：-webkit-overflow-scrolling:touch;是因为这行代码启用了硬件加速特性，所以滑动很流
畅。
```

详细资料可以参考：
[《解决页面使用 overflow:scroll 在 iOS 上滑动卡顿的问题》](https://www.jianshu.com/p/1f4693d0ad2d)

#### 57.有一个高度自适应的 div，里面有两个 div，一个高度 100px，希望另一个填满剩下的高度。

```
（1）外层div使用position：relative；高度要求自适应的div使用position:absolute;top:100px;bottom:0;
left:0;right:0;

（2）使用flex布局，设置主轴为竖轴，第二个div的flex-grow为1。
```

详细资料可以参考：
[《有一个高度自适应的 div，里面有两个 div，一个高度 100px，希望另一个填满剩下的高度(三种方案)》](https://blog.csdn.net/xutongbao/article/details/79408522)

#### 58.png、jpg、gif 这些图片格式解释一下，分别什么时候用。有没有了解过 webp？

相关知识点：

```
（1）BMP，是无损的、既支持索引色也支持直接色的、点阵图。这种图片格式几乎没有对数据进行压缩，所以BMP格式的图片通常
具有较大的文件大小。

（2）GIF是无损的、采用索引色的、点阵图。采用LZW压缩算法进行编码。文件小，是GIF格式的优点，同时，GIF格式还具
有支持动画以及透明的优点。但，GIF格式仅支持8bit的索引色，所以GIF格式适用于对色彩要求不高同时需要文件体积
较小的场景。

（3）JPEG是有损的、采用直接色的、点阵图。JPEG的图片的优点，是采用了直接色，得益于更丰富的色彩，JPEG非常适合用来
存储照片，与GIF相比，JPEG不适合用来存储企业Logo、线框类的图。因为有损压缩会导致图片模糊，而直接色的选用，
又会导致图片文件较GIF更大。

（4）PNG-8是无损的、使用索引色的、点阵图。PNG是一种比较新的图片格式，PNG-8是非常好的GIF格式替代者，在可能的
情况下，应该尽可能的使用PNG-8而不是GIF，因为在相同的图片效果下，PNG-8具有更小的文件体积。除此之外，PNG-8
还支持透明度的调节，而GIF并不支持。现在，除非需要动画的支持，否则我们没有理由使用GIF而不是PNG-8。

（5）PNG-24是无损的、使用直接色的、点阵图。PNG-24的优点在于，它压缩了图片的数据，使得同样效果的图片，PNG-24格
式的文件大小要比BMP小得多。当然，PNG24的图片还是要比JPEG、GIF、PNG-8大得多。

（6）SVG是无损的、矢量图。SVG是矢量图。这意味着SVG图片由直线和曲线以及绘制它们的方法组成。当你放大一个SVG图
片的时候，你看到的还是线和曲线，而不会出现像素点。这意味着SVG图片在放大时，不会失真，所以它非常适合用来绘制企
业Logo、Icon等。

（7）WebP是谷歌开发的一种新图片格式，WebP是同时支持有损和无损压缩的、使用直接色的、点阵图。从名字就可以看出来它是
为Web而生的，什么叫为Web而生呢？就是说相同质量的图片，WebP具有更小的文件体积。现在网站上充满了大量的图片，
如果能够降低每一个图片的文件大小，那么将大大减少浏览器和服务器之间的数据传输量，进而降低访问延迟，提升访问体验。

•在无损压缩的情况下，相同质量的WebP图片，文件大小要比PNG小26%；
•在有损压缩的情况下，具有相同图片精度的WebP图片，文件大小要比JPEG小25%~34%；
•WebP图片格式支持图片透明度，一个无损压缩的WebP图片，如果要支持透明度只需要22%的格外文件大小。

但是目前只有Chrome浏览器和Opera浏览器支持WebP格式，兼容性不太好。
```

回答：

```
我了解到的一共有七种常见的图片的格式。

（1）第一种是BMP格式，它是无损压缩的，支持索引色和直接色的点阵图。由于它基本上没有进行压缩，因此它的文件体积一般比
较大。

（2）第二种是GIF格式，它是无损压缩的使用索引色的点阵图。由于使用了LZW压缩方法，因此文件的体积很小。并且GIF还
支持动画和透明度。但因为它使用的是索引色，所以它适用于一些对颜色要求不高且需要文件体积小的场景。

（3）第三种是JPEG格式，它是有损压缩的使用直接色的点阵图。由于使用了直接色，色彩较为丰富，一般适用于来存储照片。但
由于使用的是直接色，可能文件的体积相对于GIF格式来说更大。

（4）第四种是PNG-8格式，它是无损压缩的使用索引色的点阵图。它是GIF的一种很好的替代格式，它也支持透明度的调整，并
且文件的体积相对于GIF格式更小。一般来说如果不是需要动画的情况，我们都可以使用PNG-8格式代替GIF格式。

（5）第五种是PNG-24格式，它是无损压缩的使用直接色的点阵图。PNG-24的优点是它使用了压缩算法，所以它的体积比BMP
格式的文件要小得多，但是相对于其他的几种格式，还是要大一些。

（6）第六种格式是svg格式，它是矢量图，它记录的图片的绘制方式，因此对矢量图进行放大和缩小不会产生锯齿和失真。它一般
适合于用来制作一些网站logo或者图标之类的图片。

（7）第七种格式是webp格式，它是支持有损和无损两种压缩方式的使用直接色的点阵图。使用webp格式的最大的优点是，在相
同质量的文件下，它拥有更小的文件体积。因此它非常适合于网络图片的传输，因为图片体积的减少，意味着请求时间的减小，
这样会提高用户的体验。这是谷歌开发的一种新的图片格式，目前在兼容性上还不是太好。
```

详细资料可以参考：
[《图片格式那么多，哪种更适合你？》](https://www.cnblogs.com/xinzhao/p/5130410.html)

#### 59.浏览器如何判断是否支持 webp 格式图片

```
（1）宽高判断法。通过创建image对象，将其src属性设置为webp格式的图片，然后在onload事件中获取图片的宽高，如
果能够获取，则说明浏览器支持webp格式图片。如果不能获取或者触发了onerror函数，那么就说明浏览器不支持webp格
式的图片。

（2）canvas判断方法。我们可以动态的创建一个canvas对象，通过canvas的toDataURL将设置为webp格式，然后判断
返回值中是否含有image/webp字段，如果包含则说明支持WebP，反之则不支持。
```

详细资料可以参考：
[《判断浏览器是否支持 WebP 图片》](https://blog.csdn.net/jesslu/article/details/82495061)
[《toDataURL()》](https://developer.mozilla.org/zh-CN/docs/Web/API/HTMLCanvasElement/toDataURL)

#### 60.什么是 Cookie 隔离？（或者说：请求资源的时候不要让它带 cookie 怎么做）

```
网站向服务器请求的时候，会自动带上cookie这样增加表头信息量，使请求变慢。

如果静态文件都放在主域名下，那静态文件请求的时候都带有的cookie的数据提交给server的，非常浪费流量，所以不如隔离开
，静态资源放CDN。

因为cookie有域的限制，因此不能跨域提交请求，故使用非主要域名的时候，请求头中就不会带有cookie数据，这样可以降低请
求头的大小，降低请求时间，从而达到降低整体请求延时的目的。

同时这种方式不会将cookie传入WebServer，也减少了WebServer对cookie的处理分析环节，提高了webserver的
http请求的解析速度。
```

详细资料可以参考：
[《CDN 是什么？使用 CDN 有什么优势？》](https://www.zhihu.com/question/36514327?rf=37353035)

#### 61.style 标签写在 body 后与 body 前有什么区别？

```
页面加载自上而下当然是先加载样式。写在body标签后由于浏览器以逐行方式对HTML文档进行解析，当解析到写在尾部的样式
表（外联或写在style标签）会导致浏览器停止之前的渲染，等待加载且解析样式表完成之后重新渲染，在windows的IE下可
能会出现FOUC现象（即样式失效导致的页面闪烁问题）
```

#### 62.什么是 CSS 预处理器/后处理器？

```
CSS预处理器定义了一种新的语言，其基本思想是，用一种专门的编程语言，为CSS增加了一些编程的特性，将CSS作为目标生成
文件，然后开发者就只要使用这种语言进行编码工作。通俗的说，CSS预处理器用一种专门的编程语言，进行Web页面样式设计，然
后再编译成正常的CSS文件。

预处理器例如：LESS、Sass、Stylus，用来预编译Sass或less csssprite，增强了css代码的复用性，还有层级、mixin、
变量、循环、函数等，具有很方便的UI组件模块化开发能力，极大的提高工作效率。

CSS后处理器是对CSS进行处理，并最终生成CSS的预处理器，它属于广义上的CSS预处理器。我们很久以前就在用CSS后
处理器了，最典型的例子是CSS压缩工具（如clean-css），只不过以前没单独拿出来说过。还有最近比较火的Autoprefixer，
以CanIUse上的浏览器支持数据为基础，自动处理兼容性问题。

后处理器例如：PostCSS，通常被视为在完成的样式表中根据CSS规范处理CSS，让其更有效；目前最常做的是给CSS属性添加浏
览器私有前缀，实现跨浏览器兼容性的问题。
```

详细资料可以参考：
[《CSS 预处理器和后处理器》](https://blog.csdn.net/yushuangyushuang/article/details/79209752)

#### 63.阐述一下 CSSSprites

```
将一个页面涉及到的所有图片都包含到一张大图中去，然后利用CSS的background-image，background-repeat，background
-position的组合进行背景定位。利用CSSSprites能很好地减少网页的http请求，从而很好的提高页面的性能；CSSSprites
能减少图片的字节。

优点：

减少HTTP请求数，极大地提高页面加载速度
增加图片信息重复度，提高压缩比，减少图片大小
更换风格方便，只需在一张或几张图片上修改颜色或样式即可实现

缺点：

图片合并麻烦
维护麻烦，修改一个图片可能需要重新布局整个图片，样式
```

#### 64.使用 rem 布局的优缺点？

```
优点：
在屏幕分辨率千差万别的时代，只要将rem与屏幕分辨率关联起来就可以实现页面的整体缩放，使得在设备上的展现都统一起来了。
而且现在浏览器基本都已经支持rem了，兼容性也非常的好。

缺点：
（1）在奇葩的dpr设备上表现效果不太好，比如一些华为的高端机型用rem布局会出现错乱。
（2）使用iframe引用也会出现问题。
（3）rem在多屏幕尺寸适配上与当前两大平台的设计哲学不一致。即大屏的出现到底是为了看得又大又清楚，还是为了看的更多的问
题。
```

详细资料可以参考：
[《css3 的字体大小单位 rem 到底好在哪？》](https://www.zhihu.com/question/21504656)
[《VW:是时候放弃 REM 布局了》](https://www.jianshu.com/p/e8ae1c3861dc)
[《为什么设计稿是 750px》](https://blog.csdn.net/Honeymao/article/details/76795089)
[《使用 Flexible 实现手淘 H5 页面的终端适配》](https://github.com/amfe/article/issues/17)

#### 65.几种常见的 CSS 布局

详细的资料可以参考：
[《几种常见的 CSS 布局》](https://juejin.im/post/5bbcd7ff5188255c80668028#heading-12)

#### 66.画一条 0.5px 的线

```
采用meta viewport的方式

采用border-image的方式

采用transform:scale()的方式
```

详细资料可以参考：
[《怎么画一条 0.5px 的边（更新）》](https://juejin.im/post/5ab65f40f265da2384408a95)

#### 67.transition 和 animation 的区别

```
transition关注的是CSS property的变化，property值和时间的关系是一个三次贝塞尔曲线。

animation作用于元素本身而不是样式属性，可以使用关键帧的概念，应该说可以实现更自由的动画效果。
```

详细资料可以参考：
[《CSSanimation 与 CSStransition 有何区别？》](https://www.zhihu.com/question/19749045)
[《CSS3Transition 和 Animation 区别及比较》](https://blog.csdn.net/cddcj/article/details/53582334)
[《CSS 动画简介》](http://www.ruanyifeng.com/blog/2014/02/css_transition_and_animation.html)
[《CSS 动画：animation、transition、transform、translate》](https://juejin.im/post/5b137e6e51882513ac201dfb)

#### 68.什么是首选最小宽度？

```
“首选最小宽度”，指的是元素最适合的最小宽度。

东亚文字（如中文）最小宽度为每个汉字的宽度。

西方文字最小宽度由特定的连续的英文字符单元决定。并不是所有的英文字符都会组成连续单元，一般会终止于空格（普通空格）、短
横线、问号以及其他非英文字符等。

如果想让英文字符和中文一样，每一个字符都用最小宽度单元，可以试试使用CSS中的word-break:break-all。
```

#### 69.为什么 height:100%会无效？

```
对于普通文档流中的元素，百分比高度值要想起作用，其父级必须有一个可以生效的高度值。

原因是如果包含块的高度没有显式指定（即高度由内容决定），并且该元素不是绝对定位，则计算值为auto，因为解释成了auto，
所以无法参与计算。

使用绝对定位的元素会有计算值，即使祖先元素的height计算为auto也是如此。
```

#### 70.min-width/max-width 和 min-height/max-height 属性间的覆盖规则？

```
（1）max-width会覆盖width，即使width是行类样式或者设置了!important。

（2）min-width会覆盖max-width，此规则发生在min-width和max-width冲突的时候。
```

#### 71.内联盒模型基本概念

```
（1）内容区域（content area）。内容区域指一种围绕文字看不见的盒子，其大小仅受字符本身特性控制，本质上是一个字符盒子
（character box）；但是有些元素，如图片这样的替换元素，其内容显然不是文字，不存在字符盒子之类的，因此，对于这些
元素，内容区域可以看成元素自身。

（2）内联盒子（inline box）。“内联盒子”不会让内容成块显示，而是排成一行，这里的“内联盒子”实际指的就是元素的“外在盒
子”，用来决定元素是内联还是块级。该盒子又可以细分为“内联盒子”和“匿名内联盒子”两类。

（3）行框盒子（line box），每一行就是一个“行框盒子”（实线框标注），每个“行框盒子”又是由一个一个“内联盒子”组成的。

（4）包含块（containing box），由一行一行的“行框盒子”组成。
```

#### 72.什么是幽灵空白节点？

```
“幽灵空白节点”是内联盒模型中非常重要的一个概念，具体指的是：在HTML5文档声明中，内联元素的所有解析和渲染表现就如同
每个行框盒子的前面有一个“空白节点”一样。这个“空白节点”永远透明，不占据任何宽度，看不见也无法通过脚本获取，就好像幽灵
一样，但又确确实实地存在，表现如同文本节点一样，因此，我称之为“幽灵空白节点”。
```

#### 73.什么是替换元素？

```
通过修改某个属性值呈现的内容就可以被替换的元素就称为“替换元素”。因此，<img>、<object>、<video>、<iframe>或者表
单元素<textarea>和<input>和<select>都是典型的替换元素。

替换元素除了内容可替换这一特性以外，还有以下一些特性。

（1）内容的外观不受页面上的CSS的影响。用专业的话讲就是在样式表现在CSS作用域之外。如何更改替换元素本身的外观需要
类似appearance属性，或者浏览器自身暴露的一些样式接口，

（2）有自己的尺寸。在Web中，很多替换元素在没有明确尺寸设定的情况下，其默认的尺寸（不包括边框）是300像素×150像
素，如<video>、<iframe>或者<canvas>等，也有少部分替换元素为0像素，如<img>图片，而表单元素的替换元素
的尺寸则和浏览器有关，没有明显的规律。

（3）在很多CSS属性上有自己的一套表现规则。比较具有代表性的就是vertical-align属性，对于替换元素和非替换元素，ve
rtical-align属性值的解释是不一样的。比方说vertical-align的默认值的baseline，很简单的属性值，基线之意，
被定义为字符x的下边缘，而替换元素的基线却被硬生生定义成了元素的下边缘。

（4）所有的替换元素都是内联水平元素，也就是替换元素和替换元素、替换元素和文字都是可以在一行显示的。但是，替换元素默认
的display值却是不一样的，有的是inline，有的是inline-block。
```

#### 74.替换元素的计算规则？

```
替换元素的尺寸从内而外分为3类：固有尺寸、HTML尺寸和CSS尺寸。

（1）固有尺寸指的是替换内容原本的尺寸。例如，图片、视频作为一个独立文件存在的时候，都是有着自己的宽度和高度的。

（2）HTML尺寸只能通过HTML原生属性改变，这些HTML原生属性包括<img>的width和height属性、<input>的s
ize属性、<textarea>的cols和rows属性等。

（3）CSS尺寸特指可以通过CSS的width和height或者max-width/min-width和max-height/min-height设置的
尺寸，对应盒尺寸中的content box。

这3层结构的计算规则具体如下

（1）如果没有CSS尺寸和HTML尺寸，则使用固有尺寸作为最终的宽高。

（2）如果没有CSS尺寸，则使用HTML尺寸作为最终的宽高。

（3）如果有CSS尺寸，则最终尺寸由CSS属性决定。

（4）如果“固有尺寸”含有固有的宽高比例，同时仅设置了宽度或仅设置了高度，则元素依然按照固有的宽高比例显示。

（5）如果上面的条件都不符合，则最终宽度表现为300像素，高度为150像素。

（6）内联替换元素和块级替换元素使用上面同一套尺寸计算规则。
```

#### 75.content 与替换元素的关系？

```
content属性生成的对象称为“匿名替换元素”。

（1）我们使用content生成的文本是无法选中、无法复制的，好像设置了user select:none声明一般，但是普通元素的文本
却可以被轻松选中。同时，content生成的文本无法被屏幕阅读设备读取，也无法被搜索引擎抓取，因此，千万不要自以为是
地把重要的文本信息使用content属性生成，因为这对可访问性和SEO都很不友好。

（2）content生成的内容不能左右:empty伪类。

（3）content动态生成值无法获取。
```

#### 76.margin:auto 的填充规则？

```
margin的'auto'可不是摆设，是具有强烈的计算意味的关键字，用来计算元素对应方向应该获得的剩余间距大小。但是触发mar
gin:auto计算有一个前提条件，就是width或height为auto时，元素是具有对应方向的自动填充特性的。

（1）如果一侧定值，一侧auto，则auto为剩余空间大小。
（2）如果两侧均是auto，则平分剩余空间。
```

#### 77.margin 无效的情形

```
（1）display计算值inline的非替换元素的垂直margin是无效的。对于内联替换元素，垂直margin有效，并且没有ma
rgin合并的问题。

（2）表格中的<tr>和<td>元素或者设置display计算值是table-cell或table-row的元素的margin都是无效的。

（3）绝对定位元素非定位方位的margin值“无效”。

（4）定高容器的子元素的margin-bottom或者宽度定死的子元素的margin-right的定位“失效”。
```

#### 78.border 的特殊性？

```
（1）border-width却不支持百分比。

（2）border-style的默认值是none，有一部分人可能会误以为是solid。这也是单纯设置border-width或border-col
or没有边框显示的原因。

（3）border-style:double的表现规则：双线宽度永远相等，中间间隔±1。

（4）border-color默认颜色就是color色值。

（5）默认background背景图片是相对于padding box定位的。
```

#### 79.什么是基线和 x-height？

```
字母x的下边缘（线）就是我们的基线。

x-height指的就是小写字母x的高度，术语描述就是基线和等分线（meanline）（也称作中线，midline）之间的距离。在C
SS世界中，middle指的是基线往上1/2x-height高度。我们可以近似理解为字母x交叉点那个位置。

ex是CSS中的一个相对单位，指的是小写字母x的高度，没错，就是指x-height。ex的价值就在其副业上不受字体和字号影
响的内联元素的垂直居中对齐效果。内联元素默认是基线对齐的，而基线就是x的底部，而1ex就是一个x的高度。
```

#### 80.line-height 的特殊性？

```
（1）对于非替换元素的纯内联元素，其可视高度完全由line-height决定。对于文本这样的纯内联元素，line-height就是高
度计算的基石，用专业说法就是指定了用来计算行框盒子高度的基础高度。

（2）内联元素的高度由固定高度和不固定高度组成，这个不固定的部分就是这里的“行距”。换句话说，line-height之所以起作
用，就是通过改变“行距”来实现的。在CSS中，“行距”分散在当前文字的上方和下方，也就是即使是第一行文字，其上方也是
有“行距”的，只不过这个“行距”的高度仅仅是完整“行距”高度的一半，因此，也被称为“半行距”。

（3）行距=line-height-font-size。

（4）border以及line-height等传统CSS属性并没有小数像素的概念。如果标注的是文字上边距，则向下取整；如果是文字下
边距，则向上取整。

（5）对于纯文本元素，line-height直接决定了最终的高度。但是，如果同时有替换元素，则line-height只能决定最小高度。

（6）对于块级元素，line-height对其本身是没有任何作用的，我们平时改变line-height，块级元素的高度跟着变化实际上是
通过改变块级元素里面内联级别元素占据的高度实现的。

（7）line-height的默认值是normal，还支持数值、百分比值以及长度值。为数值类型时，其最终的计算值是和当前font-si
ze相乘后的值。为百分比值时，其最终的计算值是和当前font-size相乘后的值。为长度值时原意不变。

（8）如果使用数值作为line-height的属性值，那么所有的子元素继承的都是这个值；但是，如果使用百分比值或者长度值作为
属性值，那么所有的子元素继承的是最终的计算值。

（9）无论内联元素line-height如何设置，最终父级元素的高度都是由数值大的那个line-height决定的。

（10）只要有“内联盒子”在，就一定会有“行框盒子”，就是每一行内联元素外面包裹的一层看不见的盒子。然后，重点来了，在每个
“行框盒子”前面有一个宽度为0的具有该元素的字体和行高属性的看不见的“幽灵空白节点”。
```

#### 81.vertical-align 的特殊性？

```
（1）vertical-align的默认值是baseline，即基线对齐，而基线的定义是字母x的下边缘。因此，内联元素默认都是沿着字
母x的下边缘对齐的。对于图片等替换元素，往往使用元素本身的下边缘作为基线。：一个inline-block元素，如果里面
没有内联元素，或者overflow不是visible，则该元素的基线就是其margin底边缘；否则其基线就是元素里面最后一行
内联元素的基线。

（2）vertical-align:top就是垂直上边缘对齐，如果是内联元素，则和这一行位置最高的内联元素的顶部对齐；如果display
计算值是table-cell的元素，我们不妨脑补成<td>元素，则和<tr>元素上边缘对齐。

（3）vertical-align:middle是中间对齐，对于内联元素，元素的垂直中心点和行框盒子基线往上1/2x-height处对齐。对
于table-cell元素，单元格填充盒子相对于外面的表格行居中对齐。

（4）vertical-align支持数值属性，根据数值的不同，相对于基线往上或往下偏移，如果是负值，往下偏移，如果是正值，往上
偏移。

（5）vertical-align属性的百分比值则是相对于line-height的计算值计算的。

（6）vertical-align起作用是有前提条件的，这个前提条件就是：只能应用于内联元素以及display值为table-cell的元
素。

（7）table-cell元素设置vertical-align垂直对齐的是子元素，但是其作用的并不是子元素，而是table-cell元素自身。
```

#### 82.overflow 的特殊性？

```
（1）一个设置了overflow:hidden声明的元素，假设同时存在border属性和padding属性，则当子元素内容超出容器宽度
高度限制的时候，剪裁的边界是border box的内边缘，而非padding box的内边缘。

（2）HTML中有两个标签是默认可以产生滚动条的，一个是根元素<html>，另一个是文本域<textarea>。

（3）滚动条会占用容器的可用宽度或高度。

（4）元素设置了overflow:hidden声明，里面内容高度溢出的时候，滚动依然存在，仅仅滚动条不存在！
```

#### 83.无依赖绝对定位是什么？

```
没有设置left/top/right/bottom属性值的绝对定位称为“无依赖绝对定位”。

无依赖绝对定位其定位的位置和没有设置position:absolute时候的位置相关。
```

#### 84.absolute 与 overflow 的关系？

```
（1）如果overflow不是定位元素，同时绝对定位元素和overflow容器之间也没有定位元素，则overflow无法对absolute
元素进行剪裁。

（2）如果overflow的属性值不是hidden而是auto或者scroll，即使绝对定位元素高宽比overflow元素高宽还要大，也
都不会出现滚动条。

（3）overflow元素自身transform的时候，Chrome和Opera浏览器下的overflow剪裁是无效的。
```

#### 85.clip 裁剪是什么？

```
所谓“可访问性隐藏”，指的是虽然内容肉眼看不见，但是其他辅助设备却能够进行识别和访问的隐藏。

clip剪裁被我称为“最佳可访问性隐藏”的另外一个原因就是，它具有更强的普遍适应性，任何元素、任何场景都可以无障碍使用。
```

#### 86.relative 的特殊性？

```
（1）相对定位元素的left/top/right/bottom的百分比值是相对于包含块计算的，而不是自身。注意，虽然定位位移是相对自身，但是百分比值的计算值不是。

（2）top和bottom这两个垂直方向的百分比值计算跟height的百分比值是一样的，都是相对高度计算的。同时，如果包含块的高度是auto，那么计算值是0，偏移无效，也就是说，如果父元素没有设定高度或者不是“格式化高度”，那么relative类似top:20%的代码等同于top:0。

（3）当相对定位元素同时应用对立方向定位值的时候，也就是top/bottom和left/right同时使用的时候，只有一个方向的定位属性会起作用。而谁起作用则是与文档流的顺序有关的，默认的文档流是自上而下、从左往右，因此top/bottom同时使用的时候，bottom失效；left/right同时使用的时候，right失效。
```

#### 87.什么是层叠上下文？

```
层叠上下文，英文称作stacking context，是HTML中的一个三维的概念。如果一个元素含有层叠上下文，我们可以理解为这个元
素在z轴上就“高人一等”。

层叠上下文元素有如下特性：

（1）层叠上下文的层叠水平要比普通元素高（原因后面会说明）。
（2）层叠上下文可以阻断元素的混合模式。
（3）层叠上下文可以嵌套，内部层叠上下文及其所有子元素均受制于外部的“层叠上下文”。
（4）每个层叠上下文和兄弟元素独立，也就是说，当进行层叠变化或渲染的时候，只需要考虑后代元素。
（5）每个层叠上下文是自成体系的，当元素发生层叠的时候，整个元素被认为是在父层叠上下文的层叠顺序中。


层叠上下文的创建：

（1）页面根元素天生具有层叠上下文，称为根层叠上下文。根层叠上下文指的是页面根元素，可以看成是<html>元素。因此，页面中所有的元素一定处于至少一个“层叠结界”中。

（2）对于position值为relative/absolute以及Firefox/IE浏览器（不包括Chrome浏览器）下含有position:fixed声明的定位元素，当其z-index值不是auto的时候，会创建层叠上下文。Chrome等WebKit内核浏览器下，position:fixed元素天然层叠上下文元素，无须z-index为数值。根据我的测试，目前IE和Firefox仍是老套路。

（3）其他一些CSS3属性，比如元素的opacity值不是1。
```

#### 88.什么是层叠水平？

```
层叠水平，英文称作stacking level，决定了同一个层叠上下文中元素在z轴上的显示顺序。

显而易见，所有的元素都有层叠水平，包括层叠上下文元素，也包括普通元素。然而，对普通元素的层叠水平探讨只局限在当前层叠上
下文元素中。
```

#### 89.元素的层叠顺序？

层叠顺序，英文称作 stacking order，表示元素发生层叠时有着特定的垂直显示顺序。

![层叠顺序](data:image/png;base64,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)

#### 90.层叠准则？

```
（1）谁大谁上：当具有明显的层叠水平标识的时候，如生效的z-index属性值，在同一个层叠上下文领域，层叠水平值大的那一个覆盖小的那一个。

（2）后来居上：当元素的层叠水平一致、层叠顺序相同的时候，在DOM流中处于后面的元素会覆盖前面的元素。
```

#### 91.font-weight 的特殊性？

```
如果使用数值作为font-weight属性值，必须是100～900的整百数。因为这里的数值仅仅是外表长得像数值，实际上是一个具有特定含义的关键字，并且这里的数值关键字和字母关键字之间是有对应关系的。
```

#### 92.text-indent 的特殊性？

```
（1）text-indent仅对第一行内联盒子内容有效。

（2）非替换元素以外的display计算值为inline的内联元素设置text-indent值无效，如果计算值inline-block/inli
ne-table则会生效。

（3）<input>标签按钮text-indent值无效。

（4）<button>标签按钮text-indent值有效。

（5）text-indent的百分比值是相对于当前元素的“包含块”计算的，而不是当前元素。
```

#### 93.letter-spacing 与字符间距？

```
letter-spacing可以用来控制字符之间的间距，这里说的“字符”包括英文字母、汉字以及空格等。

letter-spacing具有以下一些特性。

（1）继承性。
（2）默认值是normal而不是0。虽然说正常情况下，normal的计算值就是0，但两者还是有差别的，在有些场景下，letter-spacing会调整normal的计算值以实现更好的版面布局。
（3）支持负值，且值足够大的时候，会让字符形成重叠，甚至反向排列。
（4）和text-indent属性一样，无论值多大或多小，第一行一定会保留至少一个字符。
（5）支持小数值，即使0.1px也是支持的。
（6）暂不支持百分比值。
```

#### 94.word-spacing 与单词间距？

```
letter-spacing作用于所有字符，但word-spacing仅作用于空格字符。换句话说，word-spacing的作用就是增加空格的间隙
宽度。
```

#### 95.white-space 与换行和空格的控制？

```
white-space属性声明了如何处理元素内的空白字符，这类空白字符包括Space（空格）键、Enter（回车）键、Tab（制表符）
键产生的空白。因此，white-space可以决定图文内容是否在一行显示（回车空格是否生效），是否显示大段连续空白（空格是否
生效）等。

其属性值包括下面这些。
•normal：合并空白字符和换行符。
•pre：空白字符不合并，并且内容只在有换行符的地方换行。
•nowrap：该值和normal一样会合并空白字符，但不允许文本环绕。
•pre-wrap：空白字符不合并，并且内容只在有换行符的地方换行，同时允许文本环绕。
•pre-line：合并空白字符，但只在有换行符的地方换行，允许文本环绕。
```

#### 96.隐藏元素的 background-image 到底加不加载？

相关知识点：

```
根据测试，一个元素如果display计算值为none，在IE浏览器下（IE8～IE11，更高版本不确定）依然会发送图片请求，Fire
fox浏览器不会，至于Chrome和Safari浏览器则似乎更加智能一点：如果隐藏元素同时又设置了background-image，则图片
依然会去加载；如果是父元素的display计算值为none，则背景图不会请求，此时浏览器或许放心地认为这个背景图暂时是不会使
用的。

如果不是background-image，而是<img>元素，则设置display:none在所有浏览器下依旧都会请求图片资源。

还需要注意的是如果设置的样式没有对应的元素，则background-image也不会加载。hover情况下的background-image，在触
发时加载。
```

回答：

-（1）元素的背景图片

-元素本身设置 display:none，会请求图片 -父级元素设置 display:none，不会请求图片 -样式没有元素使用，不会请求
-:hover 样式下，触发时请求

-（2）img 标签图片任何情况下都会请求图片

详细资料可以参考：
[《CSS 控制前端图片 HTTP 请求的各种情况示例》](https://www.jb51.net/css/469033.html)

#### 97.如何实现单行／多行文本溢出的省略（…）？

```
/*单行文本溢出*/
p {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

/*多行文本溢出*/
p {
  position: relative;
  line-height: 1.5em;
  /*高度为需要显示的行数*行高，比如这里我们显示两行，则为3*/
  height: 3em;
  overflow: hidden;
}

p:after {
  content: '...';
  position: absolute;
  bottom: 0;
  right: 0;
  background-color: #fff;
}
```

详细资料可以参考：
[《【CSS/JS】如何实现单行／多行文本溢出的省略》](https://zhuanlan.zhihu.com/p/30707916)
[《CSS 多行文本溢出省略显示》](https://juejin.im/entry/587f453e1b69e60058555a5f)

#### 98.常见的元素隐藏方式？

-（1）使用 display:none;隐藏元素，渲染树不会包含该渲染对象，因此该元素不会在页面中占据位置，也不会响应绑定的监听事件。

-（2）使用 visibility:hidden;隐藏元素。元素在页面中仍占据空间，但是不会响应绑定的监听事件。

-（3）使用 opacity:0;将元素的透明度设置为 0，以此来实现元素的隐藏。元素在页面中仍然占据空间，并且能够响应元素绑定的监听事件。

-（4）通过使用绝对定位将元素移除可视区域内，以此来实现元素的隐藏。

-（5）通过 z-index 负值，来使其他元素遮盖住该元素，以此来实现隐藏。

-（6）通过 clip/clip-path 元素裁剪的方法来实现元素的隐藏，这种方法下，元素仍在页面中占据位置，但是不会响应绑定的监听事件。

-（7）通过 transform:scale(0,0)来将元素缩放为 0，以此来实现元素的隐藏。这种方法下，元素仍在页面中占据位置，但是不会响应绑定的监听事件。

详细资料可以参考：
[《CSS 隐藏元素的八种方法》](https://juejin.im/post/584b645a128fe10058a0d625#heading-2)

#### 99.css 实现上下固定中间自适应布局？

```
利用绝对定位实现body {
  padding: 0;
  margin: 0;
}

.header {
  position: absolute;
  top: 0;
  width: 100%;
  height: 100px;
  background: red;
}

.container {
  position: absolute;
  top: 100px;
  bottom: 100px;
  width: 100%;
  background: green;
}

.footer {
  position: absolute;
  bottom: 0;
  height: 100px;
  width: 100%;
  background: red;
}

利用flex布局实现html,
body {
  height: 100%;
}

body {
  display: flex;
  padding: 0;
  margin: 0;
  flex-direction: column;
}

.header {
  height: 100px;
  background: red;
}

.container {
  flex-grow: 1;
  background: green;
}

.footer {
  height: 100px;
  background: red;
}
```

详细资料可以参考：
[《css 实现上下固定中间自适应布局》](https://www.jianshu.com/p/30bc9751e3e8)

#### 100.css 两栏布局的实现？

相关资料：

```
/*两栏布局一般指的是页面中一共两栏，左边固定，右边自适应的布局，一共有四种实现的方式。*/
/*以左边宽度固定为200px为例*/

/*（1）利用浮动，将左边元素宽度设置为200px，并且设置向左浮动。将右边元素的margin-left设置为200px，宽度设置为auto（默认为auto，撑满整个父元素）。*/
.outer {
  height: 100px;
}

.left {
  float: left;

  height: 100px;
  width: 200px;

  background: tomato;
}

.right {
  margin-left: 200px;

  width: auto;
  height: 100px;

  background: gold;
}

/*（2）第二种是利用flex布局，将左边元素的放大和缩小比例设置为0，基础大小设置为200px。将右边的元素的放大比例设置为1，缩小比例设置为1，基础大小设置为auto。*/
.outer {
  display: flex;

  height: 100px;
}

.left {
  flex-shrink: 0;
  flex-grow: 0;
  flex-basis: 200px;

  background: tomato;
}

.right {
  flex: auto;
  /*11auto*/

  background: gold;
}

/*（3）第三种是利用绝对定位布局的方式，将父级元素设置相对定位。左边元素设置为absolute定位，并且宽度设置为
200px。将右边元素的margin-left的值设置为200px。*/
.outer {
  position: relative;

  height: 100px;
}

.left {
  position: absolute;

  width: 200px;
  height: 100px;

  background: tomato;
}

.right {
  margin-left: 200px;
  height: 100px;

  background: gold;
}

/*（4）第四种还是利用绝对定位的方式，将父级元素设置为相对定位。左边元素宽度设置为200px，右边元素设置为绝对定位，左边定位为200px，其余方向定位为0。*/
.outer {
  position: relative;

  height: 100px;
}

.left {
  width: 200px;
  height: 100px;

  background: tomato;
}

.right {
  position: absolute;

  top: 0;
  right: 0;
  bottom: 0;
  left: 200px;

  background: gold;
}
```

[《两栏布局 demo 展示》](http://cavszhouyou.top/Demo-Display/TwoColumnLayout/index.html)

回答：

两栏布局一般指的是页面中一共两栏，左边固定，右边自适应的布局，一共有四种实现的方式。

以左边宽度固定为 200px 为例

-（1）利用浮动，将左边元素宽度设置为 200px，并且设置向左浮动。将右边元素的 margin-left 设置为 200px，宽度设置为 auto（默认为 auto，撑满整个父元素）。

-（2）第二种是利用 flex 布局，将左边元素的放大和缩小比例设置为 0，基础大小设置为 200px。将右边的元素的放大比例设置为 1，缩小比例设置为 1，基础大小设置为 auto。

-（3）第三种是利用绝对定位布局的方式，将父级元素设置相对定位。左边元素设置为 absolute 定位，并且宽度设置为 200px。将右边元素的 margin-left 的值设置为 200px。

-（4）第四种还是利用绝对定位的方式，将父级元素设置为相对定位。左边元素宽度设置为 200px，右边元素设置为绝对定位，左边定位为 200px，其余方向定位为 0。

#### 101.css 三栏布局的实现？

相关资料：

```
/*三栏布局一般指的是页面中一共有三栏，左右两栏宽度固定，中间自适应的布局，一共有五种实现方式。

这里以左边宽度固定为100px，右边宽度固定为200px为例。*/

/*（1）利用绝对定位的方式，左右两栏设置为绝对定位，中间设置对应方向大小的margin的值。*/
.outer {
  position: relative;
  height: 100px;
}

.left {
  position: absolute;

  width: 100px;
  height: 100px;
  background: tomato;
}

.right {
  position: absolute;
  top: 0;
  right: 0;

  width: 200px;
  height: 100px;
  background: gold;
}

.center {
  margin-left: 100px;
  margin-right: 200px;
  height: 100px;
  background: lightgreen;
}

/*（2）利用flex布局的方式，左右两栏的放大和缩小比例都设置为0，基础大小设置为固定的大小，中间一栏设置为auto*/
.outer {
  display: flex;
  height: 100px;
}

.left {
  flex: 00100px;
  background: tomato;
}

.right {
  flex: 00200px;
  background: gold;
}

.center {
  flex: auto;
  background: lightgreen;
}

/*（3）利用浮动的方式，左右两栏设置固定大小，并设置对应方向的浮动。中间一栏设置左右两个方向的margin值，注意这种方式，中间一栏必须放到最后。*/
.outer {
  height: 100px;
}

.left {
  float: left;
  width: 100px;
  height: 100px;
  background: tomato;
}

.right {
  float: right;
  width: 200px;
  height: 100px;
  background: gold;
}

.center {
  height: 100px;
  margin-left: 100px;
  margin-right: 200px;
  background: lightgreen;
}

/*（4）圣杯布局，利用浮动和负边距来实现。父级元素设置左右的 padding，三列均设置向左浮动，中间一列放在最前面，宽度设置为父级元素的宽度，因此后面两列都被挤到了下一行，通过设置 margin 负值将其移动到上一行，再利用相对定位，定位到两边。*/
.outer {
  height: 100px;
  padding-left: 100px;
  padding-right: 200px;
}

.left {
  position: relative;
  left: -100px;

  float: left;
  margin-left: -100%;

  width: 100px;
  height: 100px;
  background: tomato;
}

.right {
  position: relative;
  left: 200px;

  float: right;
  margin-left: -200px;

  width: 200px;
  height: 100px;
  background: gold;
}

.center {
  float: left;

  width: 100%;
  height: 100px;
  background: lightgreen;
}

/*（5）双飞翼布局，双飞翼布局相对于圣杯布局来说，左右位置的保留是通过中间列的 margin 值来实现的，而不是通过父元
素的 padding 来实现的。本质上来说，也是通过浮动和外边距负值来实现的。*/

.outer {
  height: 100px;
}

.left {
  float: left;
  margin-left: -100%;

  width: 100px;
  height: 100px;
  background: tomato;
}

.right {
  float: left;
  margin-left: -200px;

  width: 200px;
  height: 100px;
  background: gold;
}

.wrapper {
  float: left;

  width: 100%;
  height: 100px;
  background: lightgreen;
}

.center {
  margin-left: 100px;
  margin-right: 200px;
  height: 100px;
}
```

[《三栏布局 demo 展示》](http://cavszhouyou.top/Demo-Display/ThreeColumnLayout/index.html)

回答：

```
三栏布局一般指的是页面中一共有三栏，左右两栏宽度固定，中间自适应的布局，一共有五种实现方式。

这里以左边宽度固定为100px，右边宽度固定为200px为例。

（1）利用绝对定位的方式，左右两栏设置为绝对定位，中间设置对应方向大小的margin的值。

（2）利用flex布局的方式，左右两栏的放大和缩小比例都设置为0，基础大小设置为固定的大小，中间一栏设置为auto。

（3）利用浮动的方式，左右两栏设置固定大小，并设置对应方向的浮动。中间一栏设置左右两个方向的margin值，注意这种方式，中间一栏必须放到最后。

（4）圣杯布局，利用浮动和负边距来实现。父级元素设置左右的padding，三列均设置向左浮动，中间一列放在最前面，宽度设置为父级元素的宽度，因此后面两列都被挤到了下一行，通过设置margin负值将其移动到上一行，再利用相对定位，定位到两边。圣杯布局中间列的宽度不能小于两边任意列的宽度，而双飞翼布局则不存在这个问题。

（5）双飞翼布局，双飞翼布局相对于圣杯布局来说，左右位置的保留是通过中间列的margin值来实现的，而不是通过父元素的padding来实现的。本质上来说，也是通过浮动和外边距负值来实现的。
```

#### 102.实现一个宽高自适应的正方形

```
/*1.第一种方式是利用vw来实现*/
.square {
  width: 10%;
  height: 10vw;
  background: tomato;
}

/*2.第二种方式是利用元素的margin/padding百分比是相对父元素width的性质来实现*/
.square {
  width: 20%;
  height: 0;
  padding-top: 20%;
  background: orange;
}

/*3.第三种方式是利用子元素的margin-top的值来实现的*/
.square {
  width: 30%;
  overflow: hidden;
  background: yellow;
}

.square::after {
  content: '';
  display: block;
  margin-top: 100%;
}
```

[《自适应正方形 demo 展示》](http://cavszhouyou.top/Demo-Display/AdaptiveSquare/index.html)

#### 103.实现一个三角形

```
/*三角形的实现原理是利用了元素边框连接处的等分原理。*/
.triangle {
  width: 0;
  height: 0;
  border-width: 100px;
  border-style: solid;
  border-color: tomatotransparenttransparenttransparent;
}
```

[《三角形 demo 展示》](http://cavszhouyou.top/Demo-Display/Triangle/index.html)

#### 104.一个自适应矩形，水平垂直居中，且宽高比为 2:1

```
/*实现原理参考自适应正方形和水平居中方式*/
.box {
  position: absolute;
  top: 0;
  right: 0;
  left: 0;
  bottom: 0;
  margin: auto;

  width: 10%;
  height: 0;
  padding-top: 20%;
  background: tomato;
}
```

#### 105.你知道 CSS 中不同属性设置为百分比%时对应的计算基准？

```
公式：当前元素某CSS属性值 = 基准 * 对应的百分比
元素的 position 为 relative 和 absolute 时，top和bottom、left和right基准分别为包含块的 height、width
元素的 position 为 fixed 时，top和bottom、left和right基准分别为初始包含块（也就是视口）的 height、width，移动设备较为复杂，基准为 Layout viewport 的 height、width
元素的 height 和 width 设置为百分比时，基准分别为包含块的 height 和 width
元素的 margin 和 padding 设置为百分比时，基准为包含块的 width（易错）
元素的 border-width，不支持百分比
元素的 text-indent，基准为包含块的 width

元素的 border-radius，基准为分别为自身的height、width
元素的 background-size，基准为分别为自身的height、width
元素的 translateX、translateY，基准为分别为自身的height、width
元素的 line-height，基准为自身的 font-size

元素的 font-size，基准为父元素字体
```

许可协议

本文采用[署名-非商业性使用-相同方式共享 4.0 国际](https://creativecommons.org/licenses/by-nc-sa/4.0/)许可协议，转载请注明出处。

- https://kitel.top/2022/10/14/CSS/