local mo = {
  transparent = true,
  icons = {
    git = {
      git = "",
      added = "",
      modified = "",
      deleted = "",
      renamed = "",
      ignored = "",
      untracked = "",
      unstaged = "",
      staged = "",
      megred = "",
      conflict = "",
      branch = "",
    },
    dap = {
      debug = "",
      signs = {
        breakpoint = "󰄛", -- md
        stopped = "󰋇", -- md
      },
      controls = {
        pause = "",
        play = "",
        step_into = "",
        step_over = "",
        step_out = "",
        step_back = "",
        restart = "",
        stop = "",
        disconnect = "",
      },
    },
    diagnostics = {
      error = "",
      warn = "",
      info = "",
      hint = "",
    },
    documents = {
      collapsed = "",
      expanded = "",
      new_file = "",
      file = "",
      files = "",
      file_symlink = "",
      folder = "󰉋", -- md
      folder_open = "󰝰", -- md
      root_folder = "",
      folder_symlink = "",
      empty_folder = "󰉖", -- md
      empty_folder_open = "󰷏", -- md

      modified = "",
      close = "󰖭",
    },
    todo = {
      fix = "",
      todo = "",
      hack = "",
      warn = "",
      perf = "",
      note = "",
      test = "",
    },
    indent = {
      dash = "┊",
      solid = "│",
      last = "└",
    },
    plugin = {
      plugin = "",
      installed = "",
      uninstalled = "",
      pedding = "",
    },
    navigation = {
      indicator = "▎",
      breadcrumb = "",
      triangle_left = "",
      triangle_right = "",
      arrows = "",
      left_half_circle_thick = "",
      right_half_circle_thick = "",
    },
    misc = {
      flash = "󰉂",
      bell = "",
      code = "",
      buffer = "",
      treesitter = "",
      telescope = "",
      fish = "󰈺", -- md
      creation = "󰙴", --md
      search = "",
      star = "",
      history = "",
      vim = "",
      exit = "",
      ellipsis = "",
      snow = "",
      palette = "",
      pulse = "",
      lazy = "󰒲 ",
      milestone = "",
      terminal = "",
      key = "",
      setting = "",
      task = "",
      markdown = "",
      clock = "",
      option = "󰘵",
      spinners = { "", "󰪞", "󰪟", "󰪠", "󰪢", "󰪣", "󰪤", "󰪥" },
      scrollbar = {
        "██",
        "▇▇",
        "▆▆",
        "▅▅",
        "▄▄",
        "▃▃",
        "▂▂",
        "▁▁",
        "  ",
      },
    },
    lsp = {
      lsp = "",
      kinds = {
        text = "",
        method = "",
        ["function"] = "",
        constructor = "",
        field = "",
        variable = "",
        class = "",
        interface = "",
        module = "", --
        property = "",
        unit = "", --
        value = "", --
        enum = "",
        keyword = "",
        snippet = "",
        color = "",
        file = "", --
        reference = "",
        folder = "", --
        enummember = "",
        constant = "",
        struct = "",
        event = "",
        operator = "",
        typeparameter = "", --

        namespace = "",
        package = "?",
        string = "",
        number = "",
        boolean = "",
        array = "",
        object = "?",
        key = "?",
        null = "?",
      },
    },
  },
  banner = [[
         .-') _     ('-.                      (`-.              _   .-')
        ( OO ) )  _(  OO)                   _(OO  )_           ( '.( OO )_
    ,--./ ,--,'  (,------.  .-'),-----. ,--(_/   ,. \  ,-.-')   ,--.   ,--.)
    |   \ |  |\   |  .---' ( OO'  .-.  '\   \   /(__/  |  |OO)  |   `.'   |
    |    \|  | )  |  |     /   |  | |  | \   \ /   /   |  |  \  |         |
    |  .     |/  (|  '--.  \_) |  |\|  |  \   '   /,   |  |(_/  |  |'.'|  |
    |  |\    |    |  .--'    \ |  | |  |   \     /__) ,|  |_.'  |  |   |  |
    |  | \   |    |  `---.    `'  '-'  '    \   /    (_|  |     |  |   |  |
    `--'  `--'    `------'      `-----'      `-'       `--'     `--'   `--'
  ]],
  palettes = {},
}

mo.border = mo.transparent and "rounded" or "none"

local M = {
  "catppuccin/nvim",
  name = "catppuccin",
  lazy = false,
  priority = 1000,
  opts = {
    flavour = mo.transparent and "mocha" or "macchiato",
    transparent_background = mo.transparent,
    styles = {
      keywords = { "bold" },
      functions = { "italic" },
    },
    integrations = {
      alpha = false,
      neogit = false,
      nvimtree = false,
      illuminate = false,
      rainbow_delimiters = false,
      dropbar = { enabled = false },
      mason = true,
      noice = true,
      notify = true,
      neotree = true,
      neotest = true,
      which_key = true,
      telescope = { style = mo.transparent and nil or "nvchad" },
    },
    custom_highlights = function(colors)
      return {
        -- custom
        PanelHeading = {
          fg = colors.lavender,
          bg = mo.transparent and colors.none or colors.crust,
          style = { "bold", "italic" },
        },

        -- lazy.nvim
        LazyH1 = {
          bg = mo.transparent and colors.none or colors.peach,
          fg = mo.transparent and colors.lavender or colors.base,
          style = { "bold" },
        },
        LazyButton = {
          bg = colors.none,
          fg = mo.transparent and colors.overlay0 or colors.subtext0,
        },
        LazyButtonActive = {
          bg = mo.transparent and colors.none or colors.overlay1,
          fg = mo.transparent and colors.lavender or colors.base,
          style = { " bold" },
        },
        LazySpecial = { fg = colors.sapphire },
        IblScope = { fg = colors.overlay1 },

        ColorColumn = { bg = colors.peach },
        CmpItemMenu = { fg = colors.subtext1 },
        MiniIndentscopeSymbol = { fg = colors.overlay0 },
        FloatBorder = {
          fg = mo.transparent and colors.blue or colors.mantle,
          bg = mo.transparent and colors.none or colors.mantle,
        },

        FloatTitle = {
          fg = mo.transparent and colors.lavender or colors.base,
          bg = mo.transparent and colors.none or colors.lavender,
        },
      }
    end,
  },
  config = function(_, opts)
    require("catppuccin").setup(opts)

    vim.cmd.colorscheme("catppuccin")
    mo.palettes = require("catppuccin.palettes").get_palette()
  end,
}

return M
