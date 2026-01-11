# POS系统 UML图表完整文档

本目录包含POS系统的完整UML设计图表，满足软件工程实践作业的所有要求。

## 📋 目录结构

```
docs/
├── README_UML_中文.md                    # 本说明文档（中文版）
├── UML_Diagrams_README.md                # 英文说明文档
│
├── 1. 用例模型 (Use Case Model)
│   ├── 01_UseCaseModel.puml              # 用例图 (Use Case Diagram)
│   ├── 01_UseCaseModel_Text.md           # 详细用例文本 (Fully Dressed Use Case)
│   ├── 01_SystemSequenceDiagram.puml     # 系统序列图-处理销售
│   └── 01_SystemSequenceDiagram_Return.puml # 系统序列图-处理退货
│
├── 2. 领域模型 (Domain Model)
│   └── 02_DomainModel_ClassDiagram.puml  # UML类图 (Class Diagram)
│
├── 3. 逻辑架构 (Logical Architecture)
│   ├── 03_LogicalArchitecture_PackageDiagram.puml # UML包图-详细模块
│   └── 03_LogicalArchitecture_Layers.puml        # UML包图-三层架构
│
└── 4. OO设计 (Object-Oriented Design)
    ├── 04_OODesign_InteractionDiagram_Sale.puml    # 交互图-处理销售
    ├── 04_OODesign_InteractionDiagram_Return.puml  # 交互图-处理退货
    └── 04_OODesign_DetailedClassDiagram.puml       # 详细类图
```

---

## 1. 用例模型 (Use Case Model)

### ✅ 1.1 用例图 (Use Case Diagram)
**文件**: `01_UseCaseModel.puml`

- 显示系统的主要用例
- 显示参与者（收银员、顾客）
- 显示用例之间的关系（包含、扩展）
- **主要用例**:
  - 处理销售 (Process Sale)
  - 处理退货 (Handle Returns)
  - 查看商品列表
  - 查看销售历史
  - 查看退货历史

### ✅ 1.2 详细用例文本 (Fully Dressed Use Case Text)
**文件**: `01_UseCaseModel_Text.md`

包含以下用例的详细描述：
- **UC-001**: 处理销售
  - 主要成功场景
  - 扩展场景
  - 前置条件和后置条件
  - 业务规则
- **UC-002**: 处理退货
- **UC-003**: 查看商品列表
- **UC-004**: 查看销售历史
- **UC-005**: 查看退货历史

### ✅ 1.3 系统序列图 (System Sequence Diagrams)
**文件**: 
- `01_SystemSequenceDiagram.puml` - 处理销售的系统序列图
- `01_SystemSequenceDiagram_Return.puml` - 处理退货的系统序列图

展示系统和参与者之间的交互序列，包括：
- 创建销售单/退货单
- 添加商品
- 完成交易
- 系统操作序列

---

## 2. 领域模型 (Domain Model)

### ✅ 2.1 UML类图 (Class Diagram)
**文件**: `02_DomainModel_ClassDiagram.puml`

展示领域模型层的所有实体类：

**类结构**:
- `Transaction` (抽象基类) - 演示继承和多态
- `Sale` (销售交易) - 继承自Transaction
- `ReturnTransaction` (退货交易) - 继承自Transaction
- `Product` (产品实体)
- `SaleItem` (销售项实体)

**关系**:
- **继承关系**: Transaction <|-- Sale, ReturnTransaction
- **组合关系**: Transaction *-- SaleItem
- **关联关系**: SaleItem --> Product

**面向对象特性**:
- ✅ 封装 (Encapsulation)
- ✅ 继承 (Inheritance)
- ✅ 多态 (Polymorphism)

---

## 3. 逻辑架构 (Logical Architecture)

### ✅ 3.1 UML包图 - 详细模块图
**文件**: `03_LogicalArchitecture_PackageDiagram.puml`

展示系统的完整架构：
- **用户界面层 (UI Layer)**
  - CLI界面 (POSUI)
  - GUI界面 (POSGUI)
- **业务逻辑层 (Service Layer)**
  - InventoryService
  - SaleService
  - ReturnService
- **领域模型层 (Domain Layer)**
  - Transaction, Sale, ReturnTransaction
  - Product, SaleItem

### ✅ 3.2 UML包图 - 三层架构概览
**文件**: `03_LogicalArchitecture_Layers.puml`

简化版的三层架构图，清晰展示：
- 各层的职责
- 层之间的依赖关系
- 分层架构原则

---

## 4. OO设计 (Object-Oriented Design)

### ✅ 4.1 UML交互图 - 处理销售
**文件**: `04_OODesign_InteractionDiagram_Sale.puml`

详细展示处理销售流程中对象之间的交互：
- POSUI、SaleService、InventoryService等对象的交互
- 方法调用序列
- 对象创建和状态变化

### ✅ 4.2 UML交互图 - 处理退货
**文件**: `04_OODesign_InteractionDiagram_Return.puml`

详细展示处理退货流程中对象之间的交互：
- ReturnService、InventoryService等对象的交互
- 库存恢复流程
- 退货完成流程

### ✅ 4.3 详细类图
**文件**: `04_OODesign_DetailedClassDiagram.puml`

包含所有层的完整类图：
- **领域模型层**: 所有实体类及其详细属性和方法
- **业务逻辑层**: 所有服务类及其详细方法
- **用户界面层**: UI类及其方法

---

## 🛠️ 如何查看图表

### 方法1: 在线PlantUML服务器（推荐）

1. 访问 http://www.plantuml.com/plantuml/uml/
2. 打开 `.puml` 文件，复制全部内容
3. 粘贴到在线编辑器
4. 自动生成并显示图表

### 方法2: Visual Studio Code

1. 安装 **PlantUML** 插件
2. 打开 `.puml` 文件
3. 按 `Alt+D` 预览图表
4. 按 `Ctrl+Shift+P` → "PlantUML: Export Current Diagram" 导出图片

### 方法3: IntelliJ IDEA

1. 安装 **PlantUML integration** 插件
2. 打开 `.puml` 文件
3. 自动预览，可导出为PNG/SVG

### 方法4: 命令行工具

```bash
# 需要Java环境
# 下载 plantuml.jar

# 生成PNG
java -jar plantuml.jar docs/01_UseCaseModel.puml

# 生成SVG（矢量图，推荐）
java -jar plantuml.jar -tsvg docs/01_UseCaseModel.puml

# 批量生成
java -jar plantuml.jar docs/*.puml
```

---

## 📊 图表清单总结

| 序号 | 图表类型 | 文件名 | 状态 |
|------|---------|--------|------|
| 1 | 用例图 | 01_UseCaseModel.puml | ✅ |
| 2 | 详细用例文本 | 01_UseCaseModel_Text.md | ✅ |
| 3 | 系统序列图-销售 | 01_SystemSequenceDiagram.puml | ✅ |
| 4 | 系统序列图-退货 | 01_SystemSequenceDiagram_Return.puml | ✅ |
| 5 | 领域模型类图 | 02_DomainModel_ClassDiagram.puml | ✅ |
| 6 | 逻辑架构包图-详细 | 03_LogicalArchitecture_PackageDiagram.puml | ✅ |
| 7 | 逻辑架构包图-三层 | 03_LogicalArchitecture_Layers.puml | ✅ |
| 8 | OO交互图-销售 | 04_OODesign_InteractionDiagram_Sale.puml | ✅ |
| 9 | OO交互图-退货 | 04_OODesign_InteractionDiagram_Return.puml | ✅ |
| 10 | OO详细类图 | 04_OODesign_DetailedClassDiagram.puml | ✅ |

**总计**: 10个图表文件 ✅

---

## ✨ 设计特点

### 1. 完整的用例模型
- ✅ 用例图展示所有用例和参与者
- ✅ 详细用例文本（Fully Dressed Use Case）
- ✅ 系统序列图展示系统交互

### 2. 清晰的领域模型
- ✅ UML类图展示实体关系
- ✅ 体现面向对象设计（封装、继承、多态）
- ✅ 清晰的类层次结构

### 3. 合理的架构设计
- ✅ 三层架构（UI层、Service层、Domain层）
- ✅ UML包图展示模块划分
- ✅ 清晰的依赖关系

### 4. 详细的OO设计
- ✅ 交互图展示对象协作
- ✅ 详细类图展示所有类和方法
- ✅ 完整的对象交互流程

---

## 📝 作业要求对照

### ✅ 1. Building use case model
- ✅ Use case diagrams (用例图)
- ✅ Fully dressed use case texts (详细用例文本)
- ✅ System Sequence Diagrams (系统序列图)

### ✅ 2. Building domain model
- ✅ UML Class diagrams (UML类图)

### ✅ 3. Logical Architecture
- ✅ UML Package Diagrams: Layers (层次包图)
- ✅ UML Package Diagrams: Modules (模块包图)

### ✅ 4. OO design
- ✅ UML Interaction Diagrams (交互图)
- ✅ Class Diagram (类图)

**所有要求均已完成！** ✅

---

## 📚 相关文档

- `README.md` - 项目总体说明
- `ARCHITECTURE.md` - 架构设计文档
- `OOP_FEATURES.md` - 面向对象特性说明
- `PROJECT_SUMMARY.md` - 项目总结

---

## 📞 使用建议

1. **查看图表**: 使用PlantUML在线服务器或VS Code插件
2. **导出图片**: 使用命令行工具批量导出为PNG或SVG
3. **文档说明**: 查看 `UML_Diagrams_README.md` 了解详细说明
4. **代码对照**: 图表与源代码完全对应，可对照查看

---

**创建日期**: 2025-01-10  
**最后更新**: 2025-01-10  
**状态**: ✅ 全部完成

