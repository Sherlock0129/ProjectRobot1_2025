# UML图表文档说明

本文档包含POS系统的完整UML设计图表，按照软件工程实践的要求组织。

## 图表清单

### 1. 用例模型 (Use Case Model)

#### 1.1 用例图
- **文件**: `01_UseCaseModel.puml`
- **内容**: 显示系统的主要用例和参与者之间的关系
- **主要用例**:
  - 处理销售 (Process Sale)
  - 处理退货 (Handle Returns)
  - 查看商品列表
  - 查看销售历史
  - 查看退货历史

#### 1.2 详细用例文本
- **文件**: `01_UseCaseModel_Text.md`
- **内容**: 详细描述每个用例的场景、前置条件、后置条件、扩展场景等
- **格式**: Fully Dressed Use Case

#### 1.3 系统序列图
- **文件**: 
  - `01_SystemSequenceDiagram.puml` (处理销售)
  - `01_SystemSequenceDiagram_Return.puml` (处理退货)
- **内容**: 展示系统和参与者之间的交互序列

---

### 2. 领域模型 (Domain Model)

#### 2.1 UML类图
- **文件**: `02_DomainModel_ClassDiagram.puml`
- **内容**: 展示领域模型层的所有实体类及其关系
- **主要类**:
  - `Transaction` (抽象基类)
  - `Sale` (销售交易)
  - `ReturnTransaction` (退货交易)
  - `Product` (产品)
  - `SaleItem` (销售项)
- **关系**:
  - 继承关系 (Transaction <|-- Sale, ReturnTransaction)
  - 组合关系 (Transaction *-- SaleItem)
  - 关联关系 (SaleItem --> Product)

---

### 3. 逻辑架构 (Logical Architecture)

#### 3.1 UML包图 - 详细模块图
- **文件**: `03_LogicalArchitecture_PackageDiagram.puml`
- **内容**: 展示系统的三层架构和各个模块之间的关系
- **层次**:
  - 用户界面层 (UI Layer)
  - 业务逻辑层 (Service Layer)
  - 领域模型层 (Domain Layer)

#### 3.2 UML包图 - 三层架构概览
- **文件**: `03_LogicalArchitecture_Layers.puml`
- **内容**: 简化版的三层架构图，展示各层的职责

---

### 4. OO设计 (Object-Oriented Design)

#### 4.1 交互图 - 处理销售
- **文件**: `04_OODesign_InteractionDiagram_Sale.puml`
- **内容**: 展示处理销售流程中对象之间的详细交互

#### 4.2 交互图 - 处理退货
- **文件**: `04_OODesign_InteractionDiagram_Return.puml`
- **内容**: 展示处理退货流程中对象之间的详细交互

#### 4.3 详细类图
- **文件**: `04_OODesign_DetailedClassDiagram.puml`
- **内容**: 包含所有层的详细类图，展示所有类的属性和方法
- **包含层次**:
  - 领域模型层 (Domain Layer)
  - 业务逻辑层 (Service Layer)
  - 用户界面层 (UI Layer)

---

## 如何查看这些图表

### 方法1: 使用在线PlantUML服务器

1. 访问 [PlantUML在线服务器](http://www.plantuml.com/plantuml/uml/)
2. 复制 `.puml` 文件的内容
3. 粘贴到在线编辑器中
4. 查看生成的图表

### 方法2: 使用Visual Studio Code插件

1. 安装 PlantUML 插件
2. 打开 `.puml` 文件
3. 使用 `Alt+D` 预览图表

### 方法3: 使用PlantUML命令行工具

```bash
# 安装PlantUML（需要Java环境）
# Windows: 下载plantuml.jar

# 生成PNG图片
java -jar plantuml.jar docs/01_UseCaseModel.puml

# 生成SVG图片
java -jar plantuml.jar -tsvg docs/01_UseCaseModel.puml
```

### 方法4: 使用IntelliJ IDEA

1. 安装 PlantUML 插件
2. 打开 `.puml` 文件
3. 自动预览或导出为图片

---

## 图表说明

### 图例说明

- **继承关系**: 使用 `--|>` 或 `<|--` 表示
- **关联关系**: 使用 `-->` 或 `--` 表示
- **组合关系**: 使用 `*--` 表示
- **依赖关系**: 使用 `..>` 或 `..` 表示

### 颜色说明

- **蓝色**: 用户界面层
- **绿色**: 业务逻辑层
- **黄色**: 领域模型层

---

## 设计模式应用

### 1. 分层架构模式 (Layered Architecture)
- 三层架构：UI层、Service层、Domain层
- 每层只关注自己的职责
- 上层可以依赖下层，下层不能依赖上层

### 2. 服务层模式 (Service Layer Pattern)
- Service类封装业务逻辑
- 协调领域模型对象完成业务操作
- 提供统一的业务接口

### 3. 领域模型模式 (Domain Model Pattern)
- 实体类表达业务概念
- 封装业务规则和数据
- 面向对象设计：封装、继承、多态

### 4. 抽象工厂模式 (部分应用)
- Transaction抽象基类
- 子类实现具体的交易类型

---

## 面向对象特性展示

### 1. 封装 (Encapsulation)
- 类的属性和方法封装在一起
- 私有方法使用下划线前缀
- 通过公共接口访问数据

### 2. 继承 (Inheritance)
- `Sale` 和 `ReturnTransaction` 继承自 `Transaction`
- 子类复用父类的代码
- 统一的接口定义

### 3. 多态 (Polymorphism)
- 抽象方法在不同子类中有不同实现
- `_generate_id()` 方法的多态实现
- `get_total_amount()` 方法的多态实现
- `complete()` 方法的多态实现

---

## 文件组织

```
docs/
├── UML_Diagrams_README.md              # 本文档
├── 01_UseCaseModel.puml                # 用例图
├── 01_UseCaseModel_Text.md             # 详细用例文本
├── 01_SystemSequenceDiagram.puml       # 系统序列图-销售
├── 01_SystemSequenceDiagram_Return.puml # 系统序列图-退货
├── 02_DomainModel_ClassDiagram.puml    # 领域模型类图
├── 03_LogicalArchitecture_PackageDiagram.puml # 逻辑架构包图
├── 03_LogicalArchitecture_Layers.puml  # 三层架构图
├── 04_OODesign_InteractionDiagram_Sale.puml   # OO设计交互图-销售
├── 04_OODesign_InteractionDiagram_Return.puml # OO设计交互图-退货
└── 04_OODesign_DetailedClassDiagram.puml      # OO设计详细类图
```

---

## 参考资料

- UML 2.5 规范
- PlantUML 文档: https://plantuml.com/
- 软件工程实践课程要求

---

## 更新日志

- 2025-01-10: 创建所有UML图表文档
- 包含完整的用例模型、领域模型、逻辑架构和OO设计图表

