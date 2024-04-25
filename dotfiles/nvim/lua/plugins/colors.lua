-- function SetColors(color)
--     color = color or "catppuccin-mocha"
--     vim.cmd.colorscheme(color)
--
--     vim.api.nvim_set_hl(0, "Normal", { bg = "none" })
--     vim.api.nvim_set_hl(0, "NormalFloat", { bg = "none" })
-- end

-- SetColors()

require("catppuccin").setup({
    flavor = "mocha",
    transparent_background = true,
    term_colors = true,
    integrations = {
        gitsigns = true,
        nvimtree = true,
        treesitter_context = true,
        telescope = true,

    }

})

vim.cmd.colorscheme("catppuccin")
