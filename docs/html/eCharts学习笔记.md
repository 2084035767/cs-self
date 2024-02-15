# eCharts学习笔记

## 1、简介

eCharts 是百度出品的一款基于 JavaScript 的数据可视化图表库，提供直观，生动，可交互，可个性化定制的数据可视化图表。最开始是由百度团队开源的，后面于2018年交由Apache基金会，称为ASF孵化项目。并于2021年1月26日正式毕业。

## 2、在 Vue 中使用

1. 首先下载 eCharts：

   ```
   COPYnpm install echarts --save
   ```

2. 全局引入 eCharts:

   ```
   COPYimport * as echarts from 'echarts';
   ```

3. 或者可以按需引入

   ```
   COPY// 引入 echarts 核心模块，核心模块提供了 echarts 使用必须要的接口。
   import * as echarts from 'echarts/core';
   // 引入柱状图图表，图表后缀都为 Chart
   import { BarChart } from 'echarts/charts';
   // 引入提示框，标题，直角坐标系，数据集，内置数据转换器组件，组件后缀都为 Component
   import {
     TitleComponent,
     TooltipComponent,
     GridComponent,
     DatasetComponent,
     DatasetComponentOption,
     TransformComponent
   } from 'echarts/components';
   // 标签自动布局，全局过渡动画等特性
   import { LabelLayout, UniversalTransition } from 'echarts/features';
   // 引入 Canvas 渲染器，注意引入 CanvasRenderer 或者 SVGRenderer 是必须的一步
   import { CanvasRenderer } from 'echarts/renderers';
   
   // 注册必须的组件
   echarts.use([
     TitleComponent,
     TooltipComponent,
     GridComponent,
     DatasetComponent,
     TransformComponent,
     BarChart,
     LabelLayout,
     UniversalTransition,
     CanvasRenderer
   ]);
   ```

## 3、基本语法结构

在使用 eCharts 之前，我们需要给它一个 DOM 容器，官方是推荐我们使用具有定义好的长和宽的一个父容器（可以是 div ）。
所以我们首先构建一个父容器 div 来存放 eCharts 图表

```
COPY<div id="billreport"
    :style="{ width: '95%', height: '500px' }"></div>
```

由于 eCharts 基于js构建的，所以只要会js的语法，eCharts的语法自然也不在话下。
而 eCharts 的基本语法结构为：

```
COPYsetup(){
const data=reactive({
    option:{
    	//图表信息
    }
})

const ech = () => {
	//绘制图表的方法
	}
}

onBeforeMount(()=>{
	//在页面渲染之前加载图表的信息
})
```

## 4、图表配置信息

图表配置信息，即 option 中的内容，在这一部分，我们将配置一系列的信息，正是这些信息生成了对应的图表。

```
COPYoption:{
	title:{
		text: "收入与支出趋势图"//图表的标题
	},
	tooltip:{//提示的信息
		trigger:'axis'//触发方式
	},
    legend: {//图例
        data: [{
        	name: '收入',
        	// 强制设置图形为圆。
        	icon: 'circle',
        	// 设置文本为红色
        	textStyle: {
            	color: 'red'
        	}
    	},
              {
        	name: '支出',
        	// 强制设置图形为圆。
        	icon: 'circle',
        	// 设置文本为红色
        	textStyle: {
            	color: 'red'
        	}
    	}]//图例的标题，分别对应 series 中的数据
    }，
    xAxis: {//配置要在x轴显示的项
        type: 'category',//'value' 数值轴，适用于连续数据。 'category' 类目轴，适用于离散的类目数据，为该类型时必须通过 data 设置类目数据。 'time' 时间轴，适用于连续的时序数据，与数值轴相比时间轴带有时间的格式化，在刻度计算上也有所不同，例如会根据跨度的范围来决定使用月，星期，日还是小时范围的刻度。 'log' 对数轴。适用于对数数据。
        boundaryGap: false,// 刻度离纵轴有无间隙，默认true有间距
        data: []//横轴坐标的值
    },
    yAxis: {//配置y轴的项，配置与x轴类似
        type: 'value'
    },
    series: [//系列列表,显示在图表中的内容
      {
        name: '收入',//系列名称
        type: 'line',//图表类型
        stack: '收入',//堆叠，如果有相同名称的会堆叠
        data: []
      },
      {
        name: '支出',
        type: 'line',
        stack: '支出',
        data: []
      }
   ]
}
```

图表类型表：

| 配置                  | 图表类型                       |
| --------------------- | ------------------------------ |
| type: ‘bar’           | 柱状/条形图                    |
| type: ‘line’          | 折线/面积图                    |
| type: ‘pie’           | 饼图                           |
| type: ‘scatter’       | 散点（气泡）图                 |
| type: ‘effectScatter’ | 带有涟漪特效动画的散点（气泡） |
| type: ‘radar’         | 雷达图                         |
| type: ‘tree’          | 树型图                         |
| type: ‘treemap’       | 树型图                         |
| type: ‘sunburst’      | 旭日图                         |
| type: ‘boxplot’       | 箱形图                         |
| type: ‘candlestick’   | K线图                          |
| type: ‘heatmap’       | 热力图                         |
| type: ‘map’           | 地图                           |
| type: ‘parallel’      | 平行坐标系的系列               |
| type: ‘lines’         | 线图                           |
| type: ‘graph’         | 关系图                         |
| type: ‘sankey’        | 桑基图                         |
| type: ‘funnel’        | 漏斗图                         |
| type: ‘gauge’         | 仪表盘                         |
| type: ‘pictorialBar’  | 象形柱图                       |
| type: ‘themeRiver’    | 主题河流                       |
| type: ‘custom’        | 自定义系列                     |

## 5、x 轴、y 轴

x 轴和 y 轴都由轴线、刻度、刻度标签、轴标题四个部分组成。
一般情况下，二维的图标结构都会有 x 轴和 y 轴，通常情况下，x 轴会在图表的下方，而 y 轴在图表的左边。
而 eCharts 也提供了一些特定的坐标轴的设置选项，如：
**轴线：**
我们可以通过 axisLine 来对轴线进行设置，比如轴线两头的箭头，轴线的样式等等，比如：

```
COPYoption = {
  xAxis: {
    axisLine: {
      show:'true' //显示轴线
      symbol: 'arrow', //轴线两边的箭头
      lineStyle: { //轴线的样式，有颜色、宽度、类型等等
        type: 'dashed'
        // ...
      }
    }
    // ...
  },
  yAxis: {
    axisLine: {
      symbol: 'arrow',
      lineStyle: {
        type: 'dashed'
        // ...
      }
    }
  }
  // ...
};
```

轴线两边的箭头选项：
![This is a picture without description](data:image/png;base64,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)

**坐标轴刻度：**
ECharts 提供了轴线 axisTick 相关的配置，我们可以根据实际情况调整，例如刻度线的长度，样式等。以下是一个坐标轴刻度的例子：

```
COPYoption = {
  xAxis: {
    axisTick: {
      show:true //开启坐标轴刻度
      alignWithLabel:true //使刻度与标签对其（类目轴中在 boundaryGap 为 true 的时候有效）
      inside:true //刻度线是否朝里（true为朝里）
      interval：0 //坐标轴刻度的显示间隔,如果设置为 1，表示『隔一个标签显示一个标签』，如果值为 2，表示隔两个标签显示一个标签，以此类推。
      length: 6,//刻度线的长度
      lineStyle: { //样式设置
        type: 'dashed'
        // ...
      }
    }
    // ...
  },
  yAxis: {
    axisTick: {
      length: 6,
      lineStyle: {
        type: 'dashed'
        // ...
      }
    }
  }
  // ...
};
```

**刻度标签：**
ECharts 提供了轴线 axisLabel 相关的配置，我们可以根据实际情况调整。以下是一个例子：
![This is a picture without description](data:image/png;base64,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)
如上图所示，下面的星期就是刻度标签

```
COPYoption = {
  xAxis: {
    axisLabel: {
      show:true //显示刻度标签
      interval:0 //显示刻度，同上
      inside:true //标签是否朝里（true朝里）
      rotate：45 // 标签偏移的角度
      margin:5 //标签与轴线的距离
      formatter: '{value} kg', //刻度标签的内容格式器，支持字符串模板和回调函数两种形式。
      align: 'center' //文字水平对齐方式，默认自动。可选为：'left','center','right'
      // ...
    }
    // ...
  },
  yAxis: {
    axisLabel: {
      formatter: '{value} 元',
      align: 'center'
      // ...
    }
  }
  // ...
};
```

**标签中的formatter：**

```
COPY// 使用字符串模板，模板变量为刻度默认标签 {value}
formatter: '{value} kg'
// 使用函数模板，函数参数分别为刻度数值（类目），刻度的索引
formatter: function (value, index) {
    return value + 'kg';
}
```

更多关于 formatter 的内容可以参考官方的 [API](https://echarts.apache.org/zh/option.html#xAxis.axisLabel.formatter)

## 6、主题配置

在eCharts的内部，内置了两套主题，分别是亮色主题以及暗色主题
通过以下的方式，我们可以修改主题

```
COPYvar chart = echarts.init(dom, 'light');
var chart = echarts.init(dom, 'dark');
```

或者我们可以通过eCharts的[主题编辑器](https://echarts.apache.org/zh/theme-builder.html)来创建自己的主题!

## 7、数据集（dataset）

dataset 组件可以用于单独的数据集声明，从而数据可以单独管理，被多个组件复用，并且可以基于数据指定数据到视觉的映射。

**写法一：**

```
COPYdataset: {
    // 提供一份数据。
    //第一行对应的是 x 轴
    source: [
        ['product', '2015', '2016', '2017'],
        ['Matcha Latte', 43.3, 85.8, 93.7],
        ['Milk Tea', 83.1, 73.4, 55.1],
        ['Cheese Cocoa', 86.4, 65.2, 82.5],
        ['Walnut Brownie', 72.4, 53.9, 39.1]
    ]
},
```

在 dataset 中管理数据之后，就可以不用在 series 单独进行数据的声明，而是直接在 data 除进行调用

```
COPY// 声明多个柱状图系列，默认情况下，每个系列会自动对应到 dataset 的每一列。
series: [
    {type: 'bar'},
    {type: 'bar'},
    {type: 'bar'}
]
```

**写法二：**

```
COPYdataset: {
    // 这里指定了维度名的顺序，从而可以利用默认的维度到坐标轴的映射。
    // 如果不指定 dimensions，也可以通过指定 series.encode 完成映射，参见后文。
    dimensions: ['product', '2015', '2016', '2017'],
        source: [
            {product: 'Matcha Latte', '2015': 43.3, '2016': 85.8, '2017': 93.7},
            {product: 'Milk Tea', '2015': 83.1, '2016': 73.4, '2017': 55.1},
            {product: 'Cheese Cocoa', '2015': 86.4, '2016': 65.2, '2017': 82.5},
            {product: 'Walnut Brownie', '2015': 72.4, '2016': 53.9, '2017': 39.1}
        ]
},
```

## 8、图例

图例是图表中对内容区元素的注释、用不同形状、颜色、文字等来标示不同数据列，通过点击对应数据列的标记，可以显示或隐藏该数据列。图例虽然不是图表中的主要信息、却是了解图表信息的钥匙。
以下是一个例子：

```
COPYoption = {
  legend: {
    type:'plain' //图例的类型可选值：'scroll'：可滚动翻页的图例。当图例数量较多时可以使用。
    // Try 'horizontal'
    orient: 'vertical', //图例列表的布局朝向。可选：'horizontal'水平，'vertical'垂直
    right: 10, //图例组件离容器右侧的距离。
    top: 'center' //图例组件离容器上侧的距离。
  },
  dataset: {
    source: [
      ['product', '2015', '2016', '2017'],
      ['Matcha Latte', 43.3, 85.8, 93.7],
      ['Milk Tea', 83.1, 73.4, 55.1],
      ['Cheese Cocoa', 86.4, 65.2, 82.5],
      ['Walnut Brownie', 72.4, 53.9, 39.1]
    ]
  },
  xAxis: { type: 'category' },
  yAxis: {},
  series: [{ type: 'bar' }, { type: 'bar' }, { type: 'bar' }]
};
```

显示内容如下：![This is a picture without description](data:image/png;base64,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)
更多内容参考官方 [API](https://echarts.apache.org/zh/option.html#legend)

> 博客内容遵循 署名-非商业性使用-相同方式共享 4.0 国际 (CC BY-NC-SA 4.0) 协议
>
> 本文永久链接是：[http://cyc0819.top/2021/11/27/2021-11-27-eCharts%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0/](http://cyc0819.top/2021/11/27/2021-11-27-eCharts学习笔记/)