CodEnabled = false
local togglecod = function()
  CodEnabled = not CodEnabled
  vim.cmd([[Codeium Toggle]])
end
return {
  "Exafunction/codeium.vim",
  event = "BufEnter",
  cmd = "Codeium",
  build = ":Codeium Auth",
  opts = {},
  config = function()
    vim.keymap.set('i', '<C-e>', function() return vim.fn['codeium#Accept']() end, { expr = true, silent = true })
    vim.keymap.set('i', '<C-b>', togglecod, { expr = true, silent = true })
  end,

}
