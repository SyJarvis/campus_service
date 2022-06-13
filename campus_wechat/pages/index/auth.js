const app = getApp();

Page({

    /**
     * 页面的初始数据
     */
    data: {

        school_index: 0,
        college_index: 0,
        class_index: 0,
        schools: ['广东工贸职业技术学院', '广东番禺职业技术学院'],
        colleges: ['计算机与信息工程学院', '工商管理学院'],
        class: ['21软件7班', '21软件6班'],
        StuNum: '',
        name: '',
    },

    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function (options) {
        console.log('eeeee');
    },

    /**
     * 生命周期函数--监听页面初次渲染完成
     */
    onReady: function () {

    },

    /**
     * 生命周期函数--监听页面显示
     */
    onShow: function () {

    },
    SchoolChange(e) {
        console.log(e);
        this.setData({
            school_index: e.detail.value
        })
    },
    CollageChange(e) {
        console.log(e);
        this.setData({
            collage_index: e.detail.value
        })
    },
    ClassChange(e) {
        console.log(e);
        this.setData({
            class_index: e.detail.value
        })
    },
    getStuNum(e) {
        console.log(e)
        this.setData({
            StuNum: e.detail.value
        })
    },
    getName(e) {
        console.log(e)
        this.setData({
            name: e.detail.value
        })
    },
    goToIndex:function(){
        wx.switchTab({
          url: '/pages/index/class',
        })
    },
    AuthBind: function () {
        // 信息绑定
        var that = this;
        console.log(app.getRequestHeader());
        wx.request({
            url: app.buildUrl('/member/auth_bind'),
            header: app.getRequestHeader(),
            data: {
                school: that.data.schools[that.data.school_index],
                college: that.data.colleges[that.data.college_index],
                class: that.data.class[that.data.class_index],
                name: that.data.name,
                StuNum: that.data.StuNum
            },
            method: 'POST',
            success: function (res) {
                if (res.data.code != 200) {
                    console.log(res.data.msg);
                    app.alert({
                        'content': '未查找学生信息，请重试'
                    });
                    return;
                }
                console.log(res.data.data.token);
                app.setCache("token", res.data.data.token);
                app.tip({'title':'绑定成功', 'icon': 'success', 'duration': 2000})
                setTimeout(function(){
                    that.goToIndex();
                }, 2000) 
                
            }
        })
    }


})