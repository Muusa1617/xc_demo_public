```
题目：使用python搭建一个后台服务，并部署到linux系统上


需要实现几个接口功能
1.公告信息获取接口（需要可以编辑公告信息）
2.用户订单号生成(订单号保证唯一)
3.用户文件上传和用户文件下载接口(一个用户只允许保存一个文件，新文件会覆盖旧文件)
4.用户游戏兑换码接口(生成和领取)


最终需要上交的内容为：项目代码，系统框架结构图
```

##测试须知：
可导入xc_demo_test.json文件进行测试

服务已经部署在1.12.66.188:8000

具体内容：
ps：测试账密：q1,q1
- 公告
    - notice/describe 查询公告接口
    - notice/modify 修改公告接口，入参msg
- 订单
    - order/new_order_id 生成一个唯一订单号，供其他业务嗲用
- 文件
    - cos/upload 上传文件，入参username、password、data
    - cos/download 下载文件 入参file_name
    - 以上两个接口会校验账号密码是否正确
- 兑换码
    - 添加一个兑换码，默认可重复，入参git_code,默认可重复
    - 使用兑换码，入参username、password、gift_code
    
    


