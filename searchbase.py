
qq([keywords]){
    http://v.qq.com/x/search/?q=[keywords]
    Onsearch=True
}
youku([keywords]){
    http://www.soku.com/search_video/q_[keywords]
    Onsearch=True
}
tudou([keywords]){
    http://www.soku.com/t/nisearch.do?kw=[keywords]
    Onsearch=True
}
le([keywords]){
    http://so.le.com/s?wd=[keywords]
    Onsearch=True
}
iqiyi([keywords])(
    addr=http://so.iqiyi.com/so/q_[keywords]
    Onsearch=False
    keyword="类型： 单曲MV"
)
yinyuetai(
    addr=http://so.yinyuetai.com/mv?keyword=[keywords]
    Onsearch=True
)
wunyinyue(
    addr=http://music.163.com/#/search/m/?s=battle
    Onsearch=False
    Onplay=False
    Nextstep=True
    )
xiami(
    waitting=True
)