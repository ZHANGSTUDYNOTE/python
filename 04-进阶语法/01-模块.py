# 1-定义导入的路径
import sys
import test

sys.path.append('../test')

# 2-重新加载模块[动态更新]
import imp

imp.reload(test)
