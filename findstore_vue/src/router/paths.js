export default [
  {
    path: "",
    view: "Home",
    name: "home"
  },
  // 유저
  {
    path: "/signup",
    view: "accounts/Signup",
    name: "signup"
  },
  {
    path: "/update",
    view: "accounts/Update",
    name: "update"
  },
  {
    path: "/detail",
    view: "accounts/Detail",
    name: "detail"
  },
  // Article
  {
    path: "/article",
    view: "articles/ArticleList",
    name: "articlelist"
  },
  // meeting
  {
    path: "/meeting",
    view: "meeting/MeetingMain",
    name: "meetingmain"
  },
  {
    path: "/meeting",
    view: "meeting/MeetingList",
    name: "meetinglist"
  },
  // store
  {
    path: "/store",
    view: "stores/StoreDetail",
    name: "storedetail"
  },
];